# Five Projects With Hardware-Diversity Goals

This brief lists projects that, in different ways, resist a single dominant hardware profile. Some are blockchains, while others are distributed-computing systems whose incentives or design choices make hardware diversity useful.

| Project | URL | Hardware-diversity mechanism | How RustChain differs |
| --- | --- | --- | --- |
| Monero | https://www.getmonero.org/ | RandomX is optimized for general-purpose CPUs to reduce ASIC advantage. | Monero focuses on ASIC resistance for mining fairness; RustChain explicitly scores real hardware identity and antiquity. |
| Gridcoin | https://gridcoin.us/ | Rewards BOINC scientific computing, which runs across many CPU/GPU types. | Gridcoin rewards useful scientific work; RustChain rewards attested machine presence and hardware diversity directly. |
| Golem Network | https://www.golem.network/ | Marketplace for heterogeneous compute providers. Different jobs fit different machines. | Golem is a compute market; RustChain is a consensus/reward ledger with antiquity multipliers. |
| Akash Network | https://akash.network/ | Decentralized cloud providers contribute varied server hardware. | Akash sells deployable compute capacity; RustChain pays miners for verified hardware participation. |
| Folding@home | https://foldingathome.org/ | Distributed research workloads run across CPUs and GPUs from volunteers worldwide. | Folding@home is not a blockchain incentive system; RustChain adds a token ledger and consensus model around hardware identity. |

## Notes

Monero is the closest cryptocurrency comparison because it intentionally tries to keep commodity CPUs relevant. Its design does not care whether a CPU is old, rare, or historically interesting; it mainly wants efficient general-purpose computation to compete with specialized hardware.

Gridcoin and Folding@home show another path: diverse hardware is valuable when the workload itself can be split across many contributors. The reward or reputation comes from completed computation rather than from proving machine identity.

Golem and Akash turn heterogeneity into a marketplace feature. A provider might offer cheap CPU, high-memory servers, GPUs, or regional capacity. Diversity matters because buyers have different workloads.

RustChain is distinct because the hardware profile is part of the reward logic. A vintage or unusual machine is not merely tolerated; it can be treated as more valuable to the network's identity and decentralization goals. That makes the hard problem narrower and sharper: the network must keep hardware attestation difficult to fake while remaining usable for real, quirky machines.
