from google import genai
from dotenv import load_dotenv
import json
import os

load_dotenv()

api_key =os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in .env"
    )

client = genai.client(api_key=api_key)

def create_plan(user_input):
    """Create a plan based on the user's input using the Gemini API."""
    
    prompt = f"""
You are the planning system of a personal AI agent.

Break the user's request into a sequence of
small executable tasks.

Available actions:

- search_pdf
- calculate
- remember
- answer

Rules:

1. Create only the tasks that are necessary.
2. Put tasks in the correct order.
3. If a calculation is required, use "calculate".
4. If information from a PDF is required, use "search_pdf".
5. The final task should normally be "answer".
6. Return ONLY valid JSON.

Format:

{{
    "tasks": [
        {{
            "step": 1,
            "action": "search_pdf",
            "input": "topic"
        }},
        {{
            "step": 2,
            "action": "calculate",
            "input": "25 * 4"
        }},
        {{
            "step": 3,
            "action": "answer",
            "input": ""
        }}
    ]
}}

User request:
{user_input}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    plan_text = response.text

    try:
        plan_json = json.loads(plan_text)
    except json.JSONDecodeError:
        raise ValueError(
            "The response from the Gemini API is not valid JSON."
        )

    return plan_json