# storage.py

import json
import os

def save_stories(stories, log_date):
    """
    Save the list of curated stories to logs/YYYY-MM-DD.json
    """
    if not stories:
        print("[Storage] No stories to save.")
        return

    # Format: logs/YYYY-MM-DD.json
    filename = f"logs/{log_date.isoformat()}.json"

    # Ensure logs folder exists
    os.makedirs("logs", exist_ok=True)

    # Write data
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stories, f, indent=2, ensure_ascii=False)
        print(f"[Storage] Saved {len(stories)} stories to {filename}")
    except Exception as e:
        print(f"[Storage] Failed to save stories: {e}")
