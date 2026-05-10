# Cross-Node Consensus Desync Report

**Bounty:** Scottcjn/rustchain-bounties#58  
**Wallet/miner id:** `BenItBuhner`  
**Researcher/agent:** `CodexRevenueRunner` / Beacon agent `bcn_0e3f875c04ae`  
**Test date:** 2026-05-10  
**Method:** read-only public endpoint comparison; no state-changing requests.

## Executive Summary

The two reachable advertised RustChain consensus nodes report the same software version, same epoch, and same slot, but disagree on consensus-visible state:

| Check | Primary `50.28.86.131` | Ergo anchor `50.28.86.153` | Impact |
|---|---:|---:|---|
| Version | `2.2.1-rip200` | `2.2.1-rip200` | Same release, so this is not an obvious version mismatch. |
| Epoch | `159` | `159` | Nodes claim to be in the same epoch. |
| Slot | `22912` | `22912` | Nodes claim to be at the same slot. |
| Enrolled miners | `14` | `0` | Epoch participant set diverges completely. |
| `/api/miners` count | `14` | `0` | Public active-miner view diverges completely. |
| `BenItBuhner` balance | `73.0 RTC` | `0.0 RTC` | Wallet/balance API returns contradictory ledger state. |
| `modern-sophiacore-3a168058` balance | `0.0 RTC` | `409.490434 RTC` | A second wallet diverges in the opposite direction. |
| Node 3 `76.8.228.245:8099` | no response over HTTP/HTTPS | no response | The third advertised node is unavailable to external clients. |

This is a live split-brain / database-desync condition observable without attacking production. Clients that query different nodes receive incompatible answers for the same epoch, slot, miner set, and wallet balances.

## Reproduction

Run the included read-only probe:

```bash
node rustchain-agent-deliverables/consensus_probe_readonly.mjs
```

The script only issues `GET` requests to:

- `/health`
- `/epoch`
- `/api/miners`
- `/wallet/balance?miner_id=<wallet>`

Equivalent manual checks:

```bash
curl -sk https://50.28.86.131/epoch
curl -sk https://50.28.86.153/epoch
curl -sk https://50.28.86.131/api/miners
curl -sk https://50.28.86.153/api/miners
curl -sk "https://50.28.86.131/wallet/balance?miner_id=BenItBuhner"
curl -sk "https://50.28.86.153/wallet/balance?miner_id=BenItBuhner"
```

Observed on 2026-05-10T18:10:15-05:00:

```json
// https://50.28.86.131/epoch
{"blocks_per_epoch":144,"enrolled_miners":14,"epoch":159,"epoch_pot":1.5,"slot":22912,"total_supply_rtc":8388608}

// https://50.28.86.153/epoch
{"blocks_per_epoch":144,"enrolled_miners":0,"epoch":159,"epoch_pot":1.5,"slot":22912,"total_supply_rtc":8388608}

// https://50.28.86.131/wallet/balance?miner_id=BenItBuhner
{"amount_i64":73000000,"amount_rtc":73.0,"miner_id":"BenItBuhner"}

// https://50.28.86.153/wallet/balance?miner_id=BenItBuhner
{"amount_i64":0,"amount_rtc":0.0,"miner_id":"BenItBuhner"}

// https://50.28.86.131/wallet/balance?miner_id=modern-sophiacore-3a168058
{"amount_i64":0,"amount_rtc":0.0,"miner_id":"modern-sophiacore-3a168058"}

// https://50.28.86.153/wallet/balance?miner_id=modern-sophiacore-3a168058
{"amount_i64":409490434,"amount_rtc":409.490434,"miner_id":"modern-sophiacore-3a168058"}
```

## Attack Methodology

This was a passive consensus-integrity test:

1. Query all advertised nodes for health/version to ensure the comparison is against live services.
2. Query epoch and slot metadata to establish that the reachable nodes claim to be synchronized in time.
3. Query miner and wallet state from both nodes.
4. Compare fields that should be consensus-stable for a given epoch and slot: enrolled miners, active miner set, and wallet balances.

No network partition was created, no transactions were sent, and no attestation was replayed.

## Impact

Severity: **High**.

The network currently exposes multiple public sources of truth. Depending on which node a client uses, the same wallet can appear funded or empty, and the same epoch can have 14 enrolled miners or none. This can break:

- wallet UX and balance checks,
- bounty payout verification,
- miner enrollment verification,
- explorer displays,
- downstream agent-economy jobs that trust public balance endpoints,
- any future bridge or x402 payment validation that queries a non-primary node.

If a payment processor, bridge, or bounty verifier points at the desynced node, it can reject valid balances or accept stale/incorrect balances.

## Suggested Fixes

1. Add a canonical state root to `/epoch` or `/health` and alarm when roots diverge across nodes at the same slot.
2. Include the source node id and last applied settlement/ledger height in balance and miner responses.
3. Stop advertising a node as a consensus peer for public reads if it is not caught up on miner enrollment and balances.
4. Add an external consensus probe to CI/ops that compares `/epoch`, `/api/miners`, and sampled balances across all advertised nodes.
5. If Node 2 is intended as an anchor with partial state, split its API surface so client-facing wallet/miner endpoints do not present partial data as full ledger state.
6. Investigate why Node 3 is advertised but externally unavailable on both HTTP and HTTPS at port `8099`.

## Responsible Disclosure Notes

This report is intentionally limited to passive observation. It documents a live state divergence without attempting to force desync, replay attestations, or alter node data.
