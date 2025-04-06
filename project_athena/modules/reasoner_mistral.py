import requests
import yaml

def load_config():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)

def reason_over_data(content):
    config = load_config()
    host = config["llm"]["host"]
    model = config["llm"]["model"]
    
    prompt = f"Summarize the following:\n\n{content.strip()}\n\nKey insights:"
    
    response = requests.post(
        f"{host}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    return data.get("response", "[No response from model]")
