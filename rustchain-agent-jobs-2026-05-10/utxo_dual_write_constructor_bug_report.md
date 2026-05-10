# UTXO Red-Team Report: Epoch Dual-Write Calls `UtxoDB()` Without `db_path`

Submission target: RustChain UTXO red-team bounty `bounty_rustchain-bounties_2819`

Reporter: `CodexRevenueRunner`

Wallet/miner: `BenItBuhner`

## Summary

The epoch finalization dual-write path can fail at runtime because it constructs `UtxoDB()` without the required `db_path` argument.

In `node/rustchain_v2_integrated_v2.2.1_rip200.py`, the epoch reward loop performs the account-balance update and then tries to mirror the mining reward into the UTXO layer:

```python
from utxo_db import UtxoDB
utxo_tx = {
    "tx_type": "mining_reward",
    "inputs": [],
    "outputs": [{"address": pk, "value_nrtc": amount_i64}],
    "_allow_minting": True
}
UtxoDB().apply_transaction(utxo_tx, epoch * 144, conn=conn)
```

But `node/utxo_db.py` defines the constructor as:

```python
def __init__(self, db_path: str):
    self.db_path = db_path
```

That means the live dual-write call raises:

```text
TypeError: UtxoDB.__init__() missing 1 required positional argument: 'db_path'
```

## Impact

This sits inside the explicit epoch settlement transaction. The surrounding code begins a transaction, updates `balances`, attempts the UTXO mirror, then commits only after the loop. Because the constructor error occurs before the commit, the exception path rolls the entire settlement back.

Practical effects:

1. A settlement epoch with eligible miners can fail completely once the dual-write path is exercised.
2. Account balances and the UTXO mirror cannot advance together, defeating the intended atomic migration.
3. Operators get an epoch finalization failure instead of a clean, deterministic UTXO state root.
4. The bug is a liveness failure in the reward path rather than a direct fund-theft issue, but it can block payout finality.

## Reproduction

This is directly reproducible from the function signatures:

```python
from utxo_db import UtxoDB

UtxoDB()
```

Expected result:

```text
TypeError: UtxoDB.__init__() missing 1 required positional argument: 'db_path'
```

The epoch settlement path reaches the same constructor form at `rustchain_v2_integrated_v2.2.1_rip200.py:2882`.

## Recommended Fix

Pass the same SQLite database path used by the surrounding epoch finalizer:

```python
UtxoDB(DB_PATH).apply_transaction(utxo_tx, epoch * 144, conn=conn)
```

For maintainability, create one instance before the miner loop:

```python
from utxo_db import UtxoDB

utxo_db = UtxoDB(DB_PATH)
for pk, weight in miners:
    ...
    utxo_db.apply_transaction(utxo_tx, epoch * 144, conn=conn)
```

## Regression Test

Add a settlement regression test that monkeypatches `UtxoDB.apply_transaction` and verifies epoch finalization constructs `UtxoDB` with `DB_PATH` and reaches `apply_transaction` for a mining reward. The test should fail if `UtxoDB()` is called with no arguments.

## Suggested Severity

Medium. This does not let an attacker directly mint or steal funds, but it can halt epoch reward settlement and breaks the account-to-UTXO dual-write safety property.
