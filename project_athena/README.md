## 🧠 Why project “Athena”?

The name “Athena” is inspired by the Greek goddess of wisdom and strategic warfare. It reflects the project’s goal: to develop intelligent, strategic AI agents that can reason over local data and support human decision-making.

# llm_foundations

This project sets up a foundational AI stack on the Raspberry Pi 5 using Ollama and Mistral 7B. It establishes a local large language model (LLM) runtime with full privacy, no internet dependency, and SSD-optimized performance.

## 🔧 Components

- Raspberry Pi 5 (8GB RAM)
- External 1TB SSD for model storage
- Ollama (ARM64, CPU-only runtime)
- Mistral 7B quantized model
- Terminal access via VS Code Remote SSH

## ✅ Features

- Local model inference via REST API (`localhost:11434`)
- SSD-based model cache for performance and disk longevity
- Average generation speed: ~1 token per second (CPU-only)
- Ideal setup for building future local AI agents

## 🚀 Quick Start

```bash
ollama serve
ollama run mistral
curl http://localhost:11434
