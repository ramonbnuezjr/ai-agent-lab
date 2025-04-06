# Technical Overview - llm_foundations

## Architecture

+----------------------+ | Raspberry Pi 5 (ARM) | +----------+-----------+ | 
1. [Ollama Service] 
2. Mistral 7B Model (Q4) 
3. SSD @ /mnt/ssd/ollama-models 
4. REST API @ :11434


## Key Steps

1. Installed Ollama via install.sh script
2. Fixed `--host` flag issue by removing unsupported flag
3. Moved model storage to SSD via:
   ```bash
   export OLLAMA_MODELS=/mnt/ssd/ollama-models

## Fixed SSD permissions

sudo chown -R $USER:$USER /mnt/ssd/ollama-models

## Started Ollama manually

OLLAMA_MODELS=/mnt/ssd/ollama-models ollama serve

## Downloaded Mistral model

ollama run mistral

