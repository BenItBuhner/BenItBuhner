#!/usr/bin/env node
/*
 * Read-only RustChain cross-node consensus probe.
 *
 * This script only performs GET requests against public endpoints. It does not
 * submit attestations, transfers, jobs, or any other state-changing request.
 */

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

const nodes = [
  "https://50.28.86.131",
  "https://50.28.86.153",
  "http://76.8.228.245:8099",
  "https://76.8.228.245:8099",
];

const wallets = [
  "BenItBuhner",
  "power8-s824-sophia",
  "modern-sophiacore-3a168058",
  "RTC",
];

const timeoutMs = 8000;

async function fetchJson(node, path) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  const started = Date.now();
  try {
    const response = await fetch(`${node}${path}`, { signal: controller.signal });
    const text = await response.text();
    let body;
    try {
      body = JSON.parse(text);
    } catch {
      body = text;
    }
    return {
      node,
      path,
      ok: response.ok,
      status: response.status,
      elapsed_ms: Date.now() - started,
      body,
    };
  } catch (error) {
    return {
      node,
      path,
      ok: false,
      status: null,
      elapsed_ms: Date.now() - started,
      body: { error: String(error) },
    };
  } finally {
    clearTimeout(timer);
  }
}

const paths = ["/health", "/epoch", "/api/miners"];
for (const wallet of wallets) {
  paths.push(`/wallet/balance?miner_id=${encodeURIComponent(wallet)}`);
}

const results = [];
for (const node of nodes) {
  for (const path of paths) {
    results.push(await fetchJson(node, path));
  }
}

console.log(JSON.stringify({
  probe: "rustchain-cross-node-readonly",
  generated_at_unix: Math.floor(Date.now() / 1000),
  nodes,
  wallets,
  results,
}, null, 2));
