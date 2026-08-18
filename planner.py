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
# CREATE PLAN
# ==========================================

def create_plan(user_request):

    prompt = f"""
You are the planning system of FRIDAY,
a personal AI computer agent.

User request:

{user_request}

Break the request into the smallest
reasonable sequence of actions.

Available actions include:

open_application
open_website
search_web
type_text
press_key
click_mouse
scroll

add
subtract
multiply
divide

search_pdf

create_folder
create_file
read_file
rename_path
move_path

Rules:

1. Create only the steps necessary to
   complete the user's request.

2. Each step must contain exactly:
   - step
   - action
   - arguments

3. Use the exact action names listed above.

4. Use appropriate argument names.

5. Do not execute anything.

6. Return ONLY valid JSON.

Format:

{{
    "tasks": [
        {{
            "step": 1,
            "action": "action_name",
            "arguments": {{}}
        }}
    ]
}}

Do not use Markdown.
Do not include explanations.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    text = response.text.strip()

    # ======================================
    # Remove Markdown fences
    # ======================================

    if text.startswith("```"):

        text = text.replace(
            "```json",
            ""
        )

        text = text.replace(
            "```",
            ""
        )

        text = text.strip()

    # ======================================
    # Parse JSON
    # ======================================

    try:

        plan = json.loads(text)

        return plan

    except json.JSONDecodeError:

        print(
            "\n❌ Planner returned invalid JSON:"
        )

        print(text)

        return {
            "tasks": []
        }