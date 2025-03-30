# config.py

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the new OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)
