
## 📄 `PRD.md` (Product Requirements Document)

```markdown
# Product Requirements Document - running local LLM

## 🎯 Goal

Establish a working, low-cost, offline-friendly AI stack using a Raspberry Pi 5 and an open-source LLM (Mistral 7B).

## ✅ Success Criteria

- [x] Ollama installed on Raspberry Pi 5
- [x] Mistral 7B model downloaded and running locally
- [x] SSD used as model cache
- [x] Model responds to prompts at ~1 token/sec
- [x] API available via `localhost:11434`
- [x] Documented challenges and resolutions

## 💻 Environment

- Raspberry Pi 5 with 8GB RAM
- External SSD mounted at `/mnt/ssd`
- Debian Linux (64-bit)
- Ollama v0.6.4

## 🔒 Constraints

- No GPU (CPU-only)
- Thermal throttling risk — monitored via fan behavior
- Must operate fully offline (no cloud dependency)

## 📦 Outcome

This serves as the local LLM foundation for future agent-based systems, document assistants, and AI-powered research tools.
