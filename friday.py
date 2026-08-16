from unicodedata import category

from agent_router import classify_request
from computer_loop import run_computer_loop
from web_agent import run_web_task
from utility_agent import run_utility_task

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
# NORMAL CONVERSATION
# ==========================================

def normal_conversation(user_request):

    prompt = f"""
You are FRIDAY, a helpful personal AI assistant.

Answer the user's request clearly and naturally.

User:
{user_request}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


# ==========================================
# FRIDAY
# ==========================================

def run_friday(user_request):

    print("\n🧠 FRIDAY is thinking...")

    category = classify_request(
        user_request
    )

    print(
        f"📌 Task type: {category}"
    )

    # ======================================
    # COMPUTER
    # ======================================

    if category == "computer":

        run_computer_loop(
            user_request
        )

        return

    # ======================================
    # WEB
    # ======================================

    if category == "web":

        result = run_web_task(
            user_request
        )

        print("\n🌐 FRIDAY:")

        if result.get("success", False):

            print(result)

        else:

            print("❌ Web task failed:")

            print(
                result.get(
                    "error",
                    "Unknown error"
                )
            )

        return
    
    # ======================================
# UTILITY TOOLS
# ======================================

    if category in [
    "calculator",
    "pdf",
    "file"
]:

        result = run_utility_task(
        user_request
    )

    print("\n🛠️ FRIDAY:")

    if result.get("success", False):

        print(result)

    else:

        print(
            "❌ Utility task failed:"
        )

        print(
            result.get(
                "error",
                "Unknown error"
            )
        )

    return

    # ======================================
    # NORMAL CONVERSATION
    # ======================================

    if category == "conversation":

        answer = normal_conversation(
            user_request
        )

        print("\n🤖 FRIDAY:")
        print(answer)

        return

    # ======================================
    # OTHER TASKS
    # ======================================

    print(
        f"\n⚠️ {category} system "
        "will be connected in the next lesson."
    )

# ==========================================
# MAIN LOOP
# ==========================================

print("\n====================================")
print("          🤖 FRIDAY AI")
print("====================================")

print("Type 'exit' to stop.")


while True:

    user_request = input(
        "\nYou: "
    )

    if user_request.lower().strip() == "exit":

        print("\nFRIDAY: Goodbye!")

        break

    run_friday(user_request)