# Changelog

All notable changes to this project will be documented in this file.

This project follows [Semantic Versioning](https://semver.org/).

---

## [v1.0] - 2025-03-30

### 🎉 First Official Release: *Agent_02 – Smart News Curator*

An intelligent, modular AI agent built on Raspberry Pi 5. Agent_02 fetches, filters, summarizes, and tags AI-related news with GPT-based reasoning and clean local logging.

---

### ✨ Added
- `should_summarize()` function using GPT to validate if a URL points to a real news article
- `summarize_prompt.txt` prompt template to guide GPT summaries with tone, structure, and fallback behavior
- Early return logic for `"Not a valid article"` responses to prevent invalid summaries
- `significance_prompt.txt` and `tagging_prompt.txt` with flexible templating
- Structured output stored in `logs/YYYY-MM-DD.json`
- Terminal logging for fetches, skips, and GPT logic
- GitHub-ready project layout: `.gitignore`, `README.md`, prompt templates, modular scripts

---

### 🛠 Fixed
- Submodule conflict that prevented proper folder tracking in Git
- Leaking of invalid summaries into `.json` (e.g. homepage or category pages)
- GPT summarizing category/tag pages instead of real news stories

---

### 🧼 Clean Code Structure
- Fully modular files: `main.py`, `news_fetcher.py`, `news_processor.py`, `storage.py`, `scheduler.py`, `config.py`
- Prompts stored in `prompts/` directory for flexible customization
- Environment variables securely managed via `.env`

---

### 💻 Optimized For
- Raspberry Pi 5 (Debian-based setup with virtual environments)
- Headless, CLI-driven automation
- GitHub tracking and version control

---

## Next Up: Agent_03 (Ideas)
- Trend analysis across multiple days
- GPT-generated summaries into Markdown newsletters
- Tag confidence scoring or GPT-based clustering
