# Beginner's Guide to RustChain Mining

RustChain is a Proof-of-Antiquity blockchain. Instead of making every miner compete in a pure hashrate race, it asks miners to prove what kind of machine they are running and whether that machine is alive during the current epoch. The goal is to make real hardware, especially older and unusual hardware, part of the security and culture of the network.

## The Core Idea

Traditional Proof-of-Work rewards the miner that can perform the most hashing work. RustChain still cares about participation and liveness, but it adds a hardware-attestation layer. A miner reports machine characteristics, receives a classification, and may qualify for an antiquity multiplier when the hardware is old, rare, or preservation-worthy.

The important point for beginners is that a RustChain miner is not just a wallet address. It is a wallet plus a machine identity plus repeated attestations over time.

## What Hardware Qualifies?

RustChain's theme is vintage and diverse computing. Modern machines can participate, but older machines may qualify for stronger antiquity bonuses when the verifier can classify them confidently. Examples of interesting hardware include:

- PowerPC systems such as G4 or G5 Macs
- Older x86 desktops and laptops
- ARM single-board computers
- Unusual workstations, retro systems, or restored machines

The exact multiplier depends on network rules and verifier logic. Do not assume that simply typing "G4" or "vintage" is enough. A healthy Proof-of-Antiquity system should derive or cross-check hardware traits instead of trusting self-reported labels.

## What Is an Attestation?

An attestation is a signed or submitted proof that says, in effect: "this miner is here, this is the hardware profile, and this is the current epoch or slot context." Attestations let the network decide which miners are eligible for an epoch reward.

If you stop attesting, the network should eventually treat your miner as inactive. If you attest with inconsistent or suspicious hardware data, the verifier may reject or downgrade the miner.

## Linux Setup Overview

The exact commands may change as RustChain evolves, but a typical Linux setup looks like this:

1. Install system dependencies such as Git, Python, and build tools if the miner requires them.
2. Clone the RustChain repository or download the official miner package.
3. Create or choose a wallet/miner ID.
4. Configure the miner with the node URL, wallet/miner ID, and any hardware-attestation settings.
5. Start the miner or attestation client.
6. Check the node endpoints for enrollment, epoch status, and balance.

Conceptually:

```bash
git clone https://github.com/Scottcjn/Rustchain.git
cd Rustchain
# install project-specific dependencies from the current README
# configure your miner_id / wallet
# run the miner or attestation client
```

Then check public status endpoints such as:

```bash
curl -s https://explorer.rustchain.org/health
curl -s https://explorer.rustchain.org/epoch
curl -s https://explorer.rustchain.org/api/miners
```

## First Attestation Checklist

Before expecting rewards, confirm:

- Your miner ID is unique and consistently configured.
- The node is reachable from your machine.
- Your hardware profile is detected correctly.
- The miner appears in the active miner list or epoch enrollment data.
- You understand the epoch timing and when rewards settle.

## Common Mistakes

The most common beginner mistake is expecting an immediate balance after starting the software. Epoch systems usually pay after a settlement step, not instantly. Another mistake is changing wallet or miner IDs between runs, which makes your participation look fragmented. A third is assuming every old computer automatically receives the highest multiplier; verification quality matters.

## Why Mine RustChain?

RustChain is compelling because it treats computing history as useful infrastructure. A restored machine is not just a museum piece; it can become part of a live network. For hobbyists, that makes mining feel less like an industrial contest and more like participation in a preservation economy.

The practical path is simple: start with one machine, keep your configuration stable, watch the public endpoints, and learn how attestations map to epoch rewards. Once that works, experiment with more unusual hardware and document what you learn for the next miner.
