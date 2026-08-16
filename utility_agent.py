import json
import inspect

from google import genai
from dotenv import load_dotenv
import os

from executor import execute_task
from agent_state import AgentState


# ==========================================
# GEMINI SETUP
# ==========================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ==========================================
# AGENT STATE
# ==========================================

state = AgentState()


# ==========================================
# ALLOWED UTILITY ACTIONS
# ==========================================

ALLOWED_ACTIONS = [
    "add",
    "subtract",
    "multiply",
    "divide",

    "search_pdf",

    "create_folder",
    "create_file",
    "read_file",
    "rename_path",
    "move_path"
]


# ==========================================
# GET TOOL SIGNATURES
# ==========================================

def get_tool_information():

    from executor import TOOL_REGISTRY

    information = {}

    for action in ALLOWED_ACTIONS:

        tool = TOOL_REGISTRY.get(action)

        if tool is None:
            continue

        information[action] = str(
            inspect.signature(tool)
        )

    return information


# ==========================================
# DECIDE UTILITY ACTION
# ==========================================

def decide_utility_action(user_request):

    tool_information = get_tool_information()

    prompt = f"""
You are the utility controller of a personal AI agent.

User request:

{user_request}

Available actions:

{json.dumps(tool_information, indent=2)}

Choose the correct action.

Return ONLY valid JSON.

Format:

{{
    "action": "action_name",
    "arguments": {{}}
}}

Rules:

1. Use calculator actions for mathematical operations.

2. Use search_pdf when the user asks about information
   contained in a PDF.

3. Use file actions for creating, reading, renaming,
   moving files or folders.

4. Use the exact parameter names shown in the tool
   signatures.

5. Do not invent parameter names.

6. Do not use Markdown.

7. Do not provide explanations.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    text = response.text.strip()

    # Remove Markdown fences if Gemini adds them

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

    try:

        return json.loads(text)

    except json.JSONDecodeError:

        print(
            "\n❌ Invalid utility decision:"
        )

        print(text)

        return {
            "action": "error",
            "arguments": {},
            "message": text
        }


# ==========================================
# RUN UTILITY TASK
# ==========================================

def run_utility_task(user_request):

    print(
        "\n🛠️ Utility agent started."
    )

    action = decide_utility_action(
        user_request
    )

    print(
        "\n🤖 Utility decision:"
    )

    print(action)

    if action.get("action") == "error":

        return {
            "success": False,
            "error": action.get(
                "message",
                "Invalid decision."
            )
        }

    task = {
        "action": action.get(
            "action"
        ),

        "arguments": action.get(
            "arguments",
            {}
        )
    }

    print(
        f"\n🖐️ Executing: "
        f"{task['action']}"
    )

    result = execute_task(
        task,
        state
    )

    print(
        "\nResult:"
    )

    print(result)

    return result