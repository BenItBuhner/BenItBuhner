# Beginner's Guide to RustChain Mining

RustChain is a Proof-of-Antiquity blockchain. The basic idea is that real hardware earns network rewards, and older or less common machines can receive higher multipliers because they add diversity to the network. You do not need an ASIC miner or a GPU farm. The goal is to let ordinary CPUs participate while making virtual machines and spoofed hardware less attractive.

## How Mining Works

A RustChain miner periodically attests to the network. An attestation is a signed report that says, in effect, "this wallet is running on this machine, with these observable hardware traits, at this time." The network uses those reports to decide who is eligible for epoch rewards.

An epoch is the network's reward window. During each epoch, active miners are enrolled, weighted, and paid from the epoch pot. The exact payout depends on the miner's eligibility, hardware classification, and multiplier. A modern x86 machine can still participate, but vintage or unusual machines may receive higher antiquity multipliers.

## Hardware That Qualifies

RustChain is designed for real physical hardware. A modern laptop, desktop, mini PC, Raspberry Pi, or server can all be valid. Vintage systems can be more interesting because the network intentionally values diversity. Examples include PowerPC G4/G5 systems, POWER servers, older x86 machines, SPARC, MIPS, and other less common architectures.

Virtual machines and emulators are intentionally discouraged. They may run the software, but the fingerprinting and anti-emulation checks are meant to reduce or reject rewards when the environment does not look like real hardware.

## Linux Setup

The project has published a simple installer flow:

```bash
curl -fsSL https://rustchain.org/install.sh | bash -s -- --wallet YOUR_WALLET_NAME
```

Pick a wallet name you can reuse. For a first test, choose a stable name such as `alice-thinkpad` or `garage-powerbook`. After installation, keep the miner running so it can submit attestations over time.

If you prefer to inspect the code first, clone the repository:

```bash
git clone https://github.com/Scottcjn/Rustchain.git
cd Rustchain
```

Then follow the repository's miner instructions for your platform.

## Checking Status

After the miner starts, check whether the node sees active miners:

```bash
curl -sk https://explorer.rustchain.org/api/miners
```

You can also inspect the current epoch:

```bash
curl -sk https://explorer.rustchain.org/epoch
```

Look for your wallet or miner name in the miner list. If it appears with a recent `last_attest` timestamp, the node is receiving your attestations.

## Practical Tips

Keep the machine online for long enough to prove it is stable. Use a wallet name that identifies the machine without exposing private personal information. Save your install logs and miner output, because many bounties ask for proof of hardware, attestation, or uptime. If you are using old hardware, note the CPU model, approximate year, architecture, and operating system.

RustChain mining is less about brute force and more about showing up with real hardware. That makes it a good playground for people with old machines, home labs, and curiosity about alternative consensus designs.
