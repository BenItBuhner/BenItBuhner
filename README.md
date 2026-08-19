# Bennett Buhner

I build **agent harnesses, inference fallbacks, and small tools people actually run**. Most of the work is making models hold up in real workflows: long-running loops, MCP and tool interop, and routing that fails over instead of dying on a bad upstream.

[Portfolio](https://bennett.techlitnow.com) · [X](https://x.com/BennettBuhner) · [GitHub](https://github.com/BenItBuhner)

## Building

### [Cesium](https://github.com/BenItBuhner/Cesium) — Cursor-inspired open-source agent (TypeScript)

An OSS agent surface with multiple harnesses (native, Cursor, OpenCode, Codex, and others). Self-host it, keep work running while you are away, and hook it into GitHub and Linear. This is where most of my time goes.

### [Model Proxy](https://github.com/BenItBuhner/Model-Proxy) — any model, anywhere, with fallbacks (TypeScript, Bun)

I wanted Claude Code and similar clients to talk to whatever model I actually use. Model Proxy translates OpenAI and Anthropic APIs, streams cleanly, keeps tool-calling and multimodal payloads intact, and fails over at the API key, provider, and model layers.

### [Codex Meter](https://github.com/BenItBuhner/Codex-Meter) — Android Codex usage monitor (Java)

A native Android client and widget suite for Codex allowance: rolling windows, reset times, credits, and optional notifications. Built so I could see usage on my phone without opening a browser.

## Also

- [MCP-Base](https://github.com/BenItBuhner/MCP-Base) — TypeScript MCP server template with OpenAI and Anthropic-style methods, plus streamable HTTP and local transport
- [Insta-AI-Correct](https://github.com/BenItBuhner/Insta-AI-Correct) — AutoHotkey shortcut that Groq-corrects the text you just wrote
- **Noetic** — personal WIP: local-first notes, tasks, and calendar with a first-party agent. I use it daily; the public repo is not up yet

## Stack

- **Languages:** TypeScript, JavaScript, Python, Java, CSS
- **Runtime / frameworks:** Bun, Node.js, Next.js, React, FastAPI
- **Platforms:** GitHub, Docker, Vercel, Railway, Android
