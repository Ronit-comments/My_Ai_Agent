from google import genai
from dotenv import load_dotenv
import os
import json


# --------------------------------
# Gemini setup
# --------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in .env"
    )

client = genai.Client(
    api_key=api_key
)


# --------------------------------
# Create plan
# --------------------------------

def create_plan(user_input):

    prompt = f"""
You are the planning system of a personal AI agent.

Break the user's request into small executable tasks.

Available actions:

- search_pdf
- add
- subtract
- multiply
- divide
- answer

Rules:

1. Create only necessary tasks.
2. Put tasks in the correct order.
3. Use structured arguments.
4. Do not use "calculate".
5. Use add, subtract, multiply, or divide
   for mathematical operations.
6. The final task should normally be "answer".
7. Return ONLY valid JSON.

Examples:

For:

"Calculate 25 times 4"

Return:

{{
    "tasks": [
        {{
            "step": 1,
            "action": "multiply",
            "arguments": {{
                "a": 25,
                "b": 4
            }}
        }},
        {{
            "step": 2,
            "action": "answer",
            "arguments": {{}}
        }}
    ]
}}

For:

"Search my PDF for decision trees"

Return:

{{
    "tasks": [
        {{
            "step": 1,
            "action": "search_pdf",
            "arguments": {{
                "query": "decision trees"
            }}
        }},
        {{
            "step": 2,
            "action": "answer",
            "arguments": {{}}
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

    try:

        return json.loads(response.text)

    except json.JSONDecodeError:

        print("Planner returned invalid JSON.")

        return {
            "tasks": []
        }