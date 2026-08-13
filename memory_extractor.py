from google import genai
from dotenv import load_dotenv
import os
import json


# --------------------------------
# Gemini setup
# --------------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# --------------------------------
# Analyze memory
# --------------------------------

def analyze_memory(message):

    prompt = f"""
You are a memory management system for a personal AI assistant.

Analyze the user's message and decide whether
the information should be remembered permanently.

Remember information such as:

- User preferences
- User's name
- User's goals
- User's projects
- User's skills
- Important personal settings
- Long-term plans

Do NOT remember:

- Simple greetings
- Temporary questions
- Basic calculations
- One-time commands
- Casual conversation
- Information that has no future usefulness

Return ONLY valid JSON.

Format:

{{
    "remember": true,
    "memory": "clean summary of the information"
}}

OR:

{{
    "remember": false,
    "memory": ""
}}

User message:

{message}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    try:

        result = json.loads(response.text)

        return result

    except json.JSONDecodeError:

        return {
            "remember": False,
            "memory": ""
        }