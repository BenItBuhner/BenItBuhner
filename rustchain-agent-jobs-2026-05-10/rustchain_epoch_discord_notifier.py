#!/usr/bin/env python3
"""
Discord webhook notifier for RustChain epoch settlements.

Polls /epoch and sends a Discord webhook message whenever the epoch number
changes. Configuration is provided with environment variables or CLI flags.
"""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.request

DEFAULT_NODE = "https://explorer.rustchain.org"

def get_json(url: str, timeout: int = 10) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "rustchain-epoch-notifier/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))

def post_webhook(webhook_url: str, content: str, timeout: int = 10) -> None:
    body = json.dumps({"content": content}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "rustchain-epoch-notifier/1.0"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        if response.status >= 300:
            raise RuntimeError(f"webhook returned HTTP {response.status}")

def format_epoch_message(epoch: dict, miner_count: int | None) -> str:
    parts = [
        f"RustChain epoch update: epoch {epoch.get('epoch', 'unknown')}",
        f"slot {epoch.get('slot', 'unknown')}",
        f"pot {epoch.get('epoch_pot', 'unknown')} RTC",
    ]
    if miner_count is not None:
        parts.append(f"{miner_count} miner records")
    return " | ".join(parts)

def main() -> int:
    parser = argparse.ArgumentParser(description="Send Discord messages on RustChain epoch changes.")
    parser.add_argument("--node", default=os.getenv("RUSTCHAIN_NODE", DEFAULT_NODE))
    parser.add_argument("--webhook", default=os.getenv("DISCORD_WEBHOOK_URL"))
    parser.add_argument("--interval", type=int, default=int(os.getenv("POLL_SECONDS", "600")))
    parser.add_argument("--state-file", default=os.getenv("STATE_FILE", ".rustchain_epoch_state"))
    parser.add_argument("--once", action="store_true", help="Run one poll and exit")
    args = parser.parse_args()
    if not args.webhook:
        raise SystemExit("Missing webhook. Set DISCORD_WEBHOOK_URL or pass --webhook.")
    while True:
        try:
            epoch = get_json(args.node.rstrip("/") + "/epoch")
            miners = get_json(args.node.rstrip("/") + "/api/miners")
            current_epoch = str(epoch.get("epoch"))
            previous_epoch = None
            if os.path.exists(args.state_file):
                with open(args.state_file, "r", encoding="utf-8") as fh:
                    previous_epoch = fh.read().strip()
            if current_epoch and current_epoch != previous_epoch:
                miner_count = len(miners.get("miners", [])) if isinstance(miners, dict) else None
                post_webhook(args.webhook, format_epoch_message(epoch, miner_count))
                with open(args.state_file, "w", encoding="utf-8") as fh:
                    fh.write(current_epoch)
        except (urllib.error.URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
            print(f"poll failed: {exc}")
        if args.once:
            break
        time.sleep(max(args.interval, 30))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
