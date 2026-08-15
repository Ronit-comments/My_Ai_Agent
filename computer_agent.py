from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json

from executor import execute_task
from agent_state import AgentState


# ==========================================
# Gemini Setup
# ==========================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(
    api_key=api_key
)


# ==========================================
# Agent State
# ==========================================

state = AgentState()


# ==========================================
# Available Computer Actions
# ==========================================

available_actions = """

1. open_application
   arguments:
   {
       "application": "notepad"
   }

2. open_website
   arguments:
   {
       "url": "youtube.com"
   }

3. type_text
   arguments:
   {
       "text": "Hello Friday"
   }

4. press_key
   arguments:
   {
       "key": "enter"
   }

5. click_mouse
   arguments:
   {
       "x": 500,
       "y": 300
   }

6. scroll
   arguments:
   {
       "amount": -5
   }

"""


# ==========================================
# Create Plan
# ==========================================

def create_plan(user_request):

    prompt = f"""
You are a computer-use agent.

Your job is to convert the user's request
into a sequence of computer actions.

Available actions:

{available_actions}

User request:

{user_request}

Return ONLY valid JSON.

Format:

[
    {{
        "step": 1,
        "action": "action_name",
        "arguments": {{}}
    }}
]

Do not invent actions.
"""


    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


# ==========================================
# Run Computer Agent
# ==========================================

def run_agent(user_request):

    plan_text = create_plan(user_request)

    print("\nPLAN:")
    print(plan_text)

    try:

        plan = json.loads(plan_text)

    except json.JSONDecodeError:

        return {
            "success": False,
            "error": "Gemini returned invalid JSON."
        }

    results = []

    for task in plan:

        print(
            f"\nExecuting step "
            f"{task['step']}: "
            f"{task['action']}"
        )

        result = execute_task(
            task,
            state
        )

        results.append(result)

        print("Result:", result)

    return results


# ==========================================
# Agent Loop
# ==========================================

while True:

    user_input = input("\nYou: ")

    if user_input.lower().strip() == "exit":

        print("Goodbye!")

        break

    run_agent(user_input)