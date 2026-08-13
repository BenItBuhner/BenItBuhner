# Bennett Buhner

I build **agent harnesses, evals, and inference tools** that stay reliable when the task gets long. Most of my work is about making models usable in real workflows: token-efficient loops, fallbacks that actually fire, MCP/tooling that interoperates, and systems that can run unattended without falling apart.

More writing and project notes live on [my portfolio](https://bennett.techlitnow.com).

## What I'm working on

### [Cesium](https://github.com/BenItBuhner/Cesium) — Cursor-inspired open-source agent IDE (TypeScript)

An OSS agent surface inspired by Cursor, with multiple harnesses (native, Cursor, OpenCode, and others) over ACP. Self-host it, keep work running while you're away, and hook it into GitHub and Linear for cloud-agent style loops. This is the project I spend the most time on right now.

### [Model Proxy](https://github.com/BenItBuhner/Model-Proxy) — any model, anywhere, with fallbacks (TypeScript, Bun)

I wanted Claude Code (and similar clients) to talk to whatever model I actually use. Model Proxy translates OpenAI and Anthropic APIs, streams cleanly, keeps tool-calling and multimodal payloads intact, and fails over at the API key, provider, and model layers so a single bad upstream does not kill the session.

### [OpenGoal](https://github.com/BenItBuhner/opengoal) — OpenCode fork with goal-mode (TypeScript)

A focused fork of OpenCode that adds Codex-style goal mode and other TUI/runtime improvements. Active work is v2 protocol parity, detached execution, and keeping the fork aligned with upstream.

### [Codex Meter](https://github.com/BenItBuhner/Codex-Meter) — Android Codex usage monitor (Java)

A native Android client and widget suite for Codex allowance: rolling windows, reset times, credits, and optional notifications. Built because I wanted the usage picture on my phone without opening a browser.

### Noetic — OSS notes / tasks / calendar workspace (Next.js, TypeScript)

Still a WIP, and I still use it daily. It is meant to be a local-first, open-source workspace with a first-class agent: notes, tasks, calendar, workspaces, and MCP/remote tools in one place. Public repo is not up yet.

## Also around

- [MCP-Base](https://github.com/BenItBuhner/MCP-Base) — TypeScript MCP server template with OpenAI and Anthropic-style methods, plus streamable HTTP and local transport.
- [Insta-AI-Correct](https://github.com/BenItBuhner/Insta-AI-Correct) — AutoHotkey shortcut that Groq-corrects the text you just wrote.
- [swe-agent-moe](https://github.com/BenItBuhner/swe-agent-moe) — MoE transformer experiments aimed at SWE / agentic tasks.

## Stack

- **Languages:** TypeScript, JavaScript, Python, Java, CSS
- **Runtime / frameworks:** Bun, Node.js, Next.js, React, FastAPI
- **Platforms:** GitHub, Docker, Vercel, Railway, Android

## What I am good at

- Long-running agent loops: planning, tool use, recovery, and keeping context from rotting
- Inference plumbing: API translation, streaming hygiene, fallbacks, and harness integration
- Eval / RL environments for language models, plus the boring reliability work that makes them useful
- Shipping both local tools and hosted backends that other agents can actually call
