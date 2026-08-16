from screen_tools import take_screenshot
from vision import analyze_screen

from executor import execute_task
from agent_state import AgentState

from google import genai
from dotenv import load_dotenv
import os
import json


state = AgentState()


def observe():

    print("\n👁️ Observing screen...")

    screenshot_result = take_screenshot()

    if not screenshot_result["success"]:

        return {
            "success": False,
            "error": screenshot_result["error"]
        }

    description = analyze_screen()

    print("\n🧠 Screen:")
    print(description)

    return {
        "success": True,
        "description": description
    }


def execute_action(task):

    print(
        f"\n🖐️ Executing: "
        f"{task['action']}"
    )

    result = execute_task(
        task,
        state
    )

    # Normalize result

    if isinstance(result, bool):

        result = {
            "success": result,
            "message": (
                "Action executed successfully."
                if result
                else "Action failed."
            )
        }

    elif not isinstance(result, dict):

        result = {
            "success": False,
            "error": f"Unexpected executor result: {result}"
        }

    print("\nResult:")
    print(result)

    return result


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def decide_action(user_request, screen_description):

    prompt = f"""
You are controlling a computer.

User request:
{user_request}

Current screen:
{screen_description}

Decide the next action.

Allowed actions:

open_application
open_website
type_text
press_key
click_mouse
scroll

Return ONLY valid JSON.

Do NOT use Markdown code fences.
Do NOT write ```json.
Do NOT include any explanation.

If the user's request is already completed,
return:

{{
    "action": "done",
    "arguments": {{}}
}}

Otherwise return:

{{
    "action": "action_name",
    "arguments": {{}}
}}
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

        action = json.loads(text)

        return action

    except json.JSONDecodeError:

        print("\n❌ Gemini returned invalid JSON:")
        print(text)

        return {
            "action": "error",
            "arguments": {},
            "message": text
        }


def run_computer_loop(user_request):

    max_steps = 10

    for step in range(max_steps):

        print(
            f"\n========== STEP {step + 1} =========="
        )

        # 1. Observe

        observation = observe()

        if not observation["success"]:

            print("Observation failed.")

            break

        # 2. Think

        action = decide_action(
            user_request,
            observation["description"]
        )

        print("\n🤖 Decision:")
        print(action)

        # 3. Check if finished

        if action.get("action") == "done":

            print("\n✅ Task completed.")

            break

        # 4. Execute

        task = {
            "step": step + 1,
            "action": action["action"],
            "arguments": action.get(
                "arguments",
                {}
            )
        }

        result = execute_action(task)

        # 5. Stop if execution failed

        if not result.get("success", False):

            print(
                "\n❌ Action failed."
            )

            break

    else:

        print(
            "\n⚠️ Maximum number of steps reached."
        )