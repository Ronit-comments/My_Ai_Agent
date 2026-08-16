import json

from google import genai
from dotenv import load_dotenv
import os


# ==========================================
# GEMINI SETUP
# ==========================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ==========================================
# DETERMINE TASK TYPE
# ==========================================

def classify_request(user_request):

    prompt = f"""
Classify the user's request.

User request:
{user_request}

Choose exactly ONE category:

conversation
computer
web
file
pdf
calculator

Rules:

conversation:
Normal questions, explanations, casual conversation.

computer:
Opening applications, clicking, typing, using the mouse,
interacting with the desktop or GUI.

web:
Searching the internet or opening websites.

file:
Creating, reading, moving, renaming or managing files/folders.

pdf:
Questions requiring information from a PDF.

calculator:
Mathematical calculations.

Return ONLY valid JSON.

Example:

{{
    "category": "computer"
}}

Do not use Markdown.
Do not provide explanations.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):

        text = text.replace("```json", "")
        text = text.replace("```", "")

        text = text.strip()

    try:

        result = json.loads(text)

        return result.get(
            "category",
            "conversation"
        )

    except json.JSONDecodeError:

        return "conversation"