# Changelog - llm_foundations

## [v1.0.0] - 2025-04-05

### Added
- Installed Ollama on Raspberry Pi 5
- Configured SSD model storage
- Successfully downloaded and ran Mistral 7B model
- Verified API access via `curl localhost:11434`
- Prompt-response rate: ~1 token/sec
- Created documentation: README, PRD, technical notes

### Fixed
- Removed `--host` flag from service config (not supported in v0.6.4)
- Fixed SSD write permissions for model storage

### Next
- Build `project_brain`: RAG-based assistant using Notion + local documents
