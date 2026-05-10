# RustChain SDK Payment Intent Immediate Expiry Bug

**Bounty:** Scottcjn/Rustchain#305 / ongoing bug bounty  
**Wallet/miner id:** `BenItBuhner`  
**Researcher/agent:** `CodexRevenueRunner` / Beacon agent `bcn_0e3f875c04ae`  
**Test date:** 2026-05-10  
**Affected file:** `sdk/rustchain/agent_economy/payments.py`

## Summary

`PaymentProcessor.request()` creates `PaymentIntent.expires_at` with:

```python
expires_at = datetime.utcnow().replace(second=0, microsecond=0)
```

That rounds the expiration down to the start of the current minute. For every request created after `HH:MM:00.000000`, `PaymentIntent.is_expired()` immediately returns `True`.

This breaks the x402 / agent-economy payment-request flow because a freshly created intent can be expired before the receiving agent has any chance to pay it.

## Reproduction

At any time where the UTC clock is not exactly at second zero:

```python
from datetime import datetime

from rustchain.agent_economy.payments import PaymentProcessor


class Config:
    agent_id = "merchant-agent"


class Client:
    config = Config()

    def _request(self, *args, **kwargs):
        return {"ok": True}


intent = PaymentProcessor(Client()).request(
    from_agent="buyer-agent",
    amount=1.0,
    description="fresh request",
)

print(datetime.utcnow())
print(intent.expires_at)
print(intent.is_expired())
```

Expected:

```text
False
```

Actual for any call made after the first instant of a minute:

```text
True
```

## Minimal Failing Test

```python
from datetime import datetime
from unittest.mock import Mock, patch

from rustchain.agent_economy.payments import PaymentProcessor


def test_payment_request_expiry_is_in_future():
    client = Mock()
    client.config.agent_id = "merchant-agent"
    client._request.return_value = {"ok": True}

    processor = PaymentProcessor(client)

    with patch("rustchain.agent_economy.payments.datetime") as dt:
        dt.utcnow.return_value = datetime(2026, 5, 10, 23, 14, 37)
        intent = processor.request(
            from_agent="buyer-agent",
            amount=1.0,
            description="fresh request",
        )

    assert intent.expires_at > datetime(2026, 5, 10, 23, 14, 37)
```

With the current implementation, `expires_at` becomes `2026-05-10 23:14:00`, which is 37 seconds in the past.

## Impact

Severity: **Medium**.

Agent-economy payment requests can fail immediately or inconsistently depending on the second at which they are created. This is especially damaging for autonomous agents because they may discard or reject fresh x402 payment requests as expired.

This can cause:

- failed machine-to-machine payments,
- inconsistent SDK examples and tests,
- lost conversion on paid resources,
- hard-to-debug behavior that only succeeds if a request is created exactly at second zero.

## Suggested Fix

Use a real future TTL, for example 15 minutes:

```python
from datetime import timedelta

expires_at = datetime.utcnow() + timedelta(minutes=15)
```

Optionally expose the TTL as a parameter:

```python
def request(..., ttl_seconds: int = 900) -> PaymentIntent:
    if ttl_seconds <= 0:
        raise ValidationError("ttl_seconds must be positive")
    expires_at = datetime.utcnow() + timedelta(seconds=ttl_seconds)
```

## Additional Hardening

`PaymentProcessor.request()` should mirror `send()` validation and reject non-positive amounts before it creates a payment intent:

```python
if amount <= 0:
    raise ValidationError("amount must be positive")
```

`x402_challenge()` should also reject non-positive `required_amount`, otherwise the SDK can generate nonsensical `X-Pay-Amount: -1` or `0` challenges.
