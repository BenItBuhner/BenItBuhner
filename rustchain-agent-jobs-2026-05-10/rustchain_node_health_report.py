#!/usr/bin/env python3
"""
RustChain node health reporter.

Queries the public RustChain node endpoints and prints a compact operator
status report. The script is intentionally dependency-light and handles
timeouts or partial endpoint failures without crashing the whole report.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

DEFAULT_NODE = "https://explorer.rustchain.org"
TIMEOUT_SECONDS = 10

@dataclass
class Probe:
    name: str
    path: str
    required: bool = True

PROBES = [
    Probe("Health", "/health"),
    Probe("Epoch", "/epoch"),
    Probe("Active miners", "/api/miners"),
]

def fetch_json(base_url: str, path: str, timeout: int) -> tuple[bool, Any]:
    url = base_url.rstrip("/") + path
    req = urllib.request.Request(url, headers={"User-Agent": "rustchain-health-report/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = response.read().decode("utf-8")
            return True, json.loads(payload)
    except urllib.error.HTTPError as exc:
        return False, f"HTTP {exc.code}: {exc.reason}"
    except urllib.error.URLError as exc:
        return False, f"network error: {exc.reason}"
    except TimeoutError:
        return False, f"timeout after {timeout}s"
    except json.JSONDecodeError as exc:
        return False, f"invalid JSON: {exc}"

def format_report(results: dict[str, tuple[bool, Any]]) -> str:
    lines = [
        "RustChain Node Status Report",
        f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}",
        "",
    ]
    health_ok, health = results["Health"]
    if health_ok:
        lines.append(f"Node OK: {health.get('ok', 'unknown')}")
        lines.append(f"Version: {health.get('version', 'unknown')}")
        lines.append(f"Database writable: {health.get('db_rw', 'unknown')}")
        lines.append(f"Tip age slots: {health.get('tip_age_slots', 'unknown')}")
        lines.append(f"Uptime seconds: {health.get('uptime_s', 'unknown')}")
    else:
        lines.append(f"Health check failed: {health}")
    lines.append("")
    epoch_ok, epoch = results["Epoch"]
    if epoch_ok:
        lines.append(f"Epoch: {epoch.get('epoch', 'unknown')}")
        lines.append(f"Slot: {epoch.get('slot', 'unknown')}")
        lines.append(f"Epoch pot: {epoch.get('epoch_pot', 'unknown')} RTC")
        lines.append(f"Enrolled miners: {epoch.get('enrolled_miners', 'unknown')}")
    else:
        lines.append(f"Epoch endpoint failed: {epoch}")
    lines.append("")
    miners_ok, miners_payload = results["Active miners"]
    if miners_ok:
        miners = miners_payload.get("miners", [])
        lines.append(f"Active miner records: {len(miners)}")
        for miner in miners[:10]:
            lines.append(
                "- {miner} | {family} | multiplier={multiplier} | last_attest={last}".format(
                    miner=miner.get("miner", "unknown"),
                    family=miner.get("device_family", "unknown"),
                    multiplier=miner.get("antiquity_multiplier", "unknown"),
                    last=miner.get("last_attest", "unknown"),
                )
            )
        if len(miners) > 10:
            lines.append(f"... {len(miners) - 10} more miners omitted")
    else:
        lines.append(f"Miner endpoint failed: {miners_payload}")
    failed = [name for name, (ok, _) in results.items() if not ok]
    lines.append("")
    lines.append("Overall: " + ("DEGRADED" if failed else "OK"))
    if failed:
        lines.append("Failed probes: " + ", ".join(failed))
    return "\n".join(lines)

def main() -> int:
    parser = argparse.ArgumentParser(description="Print a RustChain node status report.")
    parser.add_argument("--node", default=DEFAULT_NODE, help="Base node URL")
    parser.add_argument("--timeout", type=int, default=TIMEOUT_SECONDS, help="Per-request timeout")
    args = parser.parse_args()
    results = {probe.name: fetch_json(args.node, probe.path, args.timeout) for probe in PROBES}
    print(format_report(results))
    return 1 if any(not ok for ok, _ in results.values()) else 0

if __name__ == "__main__":
    sys.exit(main())
