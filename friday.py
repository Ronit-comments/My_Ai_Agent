from agent_router import classify_request
from computer_loop import run_computer_loop
from web_agent import run_web_task
from utility_agent import run_utility_task

from google import genai
from dotenv import load_dotenv
import os

# ==================================================
# MEMORY IMPORTS
# ==================================================

from memory_manager import (
    get_memory_context,
    remember_conversation
)


# ==================================================
# GEMINI SETUP
# ==================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in .env"
    )

client = genai.Client(
    api_key=api_key
)


# ==================================================
# NORMAL CONVERSATION
# ==================================================

def normal_conversation(user_request):

    # ----------------------------------------------
    # Get shared memory
    # ----------------------------------------------

    context = get_memory_context(
        user_request
    )


    # ----------------------------------------------
    # Create prompt
    # ----------------------------------------------

    prompt = f"""
You are FRIDAY, a helpful personal AI assistant.

Answer the user's request clearly and naturally.

Use the provided memory when it is relevant.

Do not mention the internal memory system
unless the user specifically asks about it.

------------------------------------------
MEMORY / CONVERSATION CONTEXT
------------------------------------------

{context}

------------------------------------------
CURRENT USER REQUEST
------------------------------------------

{user_request}

------------------------------------------
INSTRUCTIONS
------------------------------------------

1. Use relevant previous conversation context.

2. Use remembered information when useful.

3. Do not invent memories.

4. If the memory does not contain the answer,
   answer normally.

5. Be concise but helpful.

6. Act like a personal AI assistant named FRIDAY.
"""


    # ----------------------------------------------
    # Gemini
    # ----------------------------------------------

    response = client.models.generate_content(

        model="gemini-3.5-flash-lite",

        contents=prompt
    )

    return response.text


# ==================================================
# SAVE MEMORY SAFELY
# ==================================================

def save_friday_memory(
    user_request,
    response
):

    try:

        # Convert response to text
        # so dictionaries / other results
        # can also be stored.

        if isinstance(response, dict):

            assistant_response = str(
                response
            )

        elif response is None:

            assistant_response = (
                "Task completed by FRIDAY."
            )

        else:

            assistant_response = str(
                response
            )


        # ------------------------------------------
        # Save conversation
        # ------------------------------------------

        remember_conversation(

            user_request,

            assistant_response
        )


    except Exception as e:

        print(
            f"\n⚠️ Memory error: {e}"
        )


# ==================================================
# FRIDAY
# ==================================================

def run_friday(user_request):

    print("\n🧠 FRIDAY is thinking...")


    # ==================================================
    # CLASSIFY REQUEST
    # ==================================================

    category = classify_request(
        user_request
    )


    print(
        f"📌 Task type: {category}"
    )


    # ==================================================
    # COMPUTER
    # ==================================================

    if category == "computer":

        try:

            result = run_computer_loop(
                user_request
            )

            # --------------------------------------
            # Save computer task to memory
            # --------------------------------------

            save_friday_memory(
                user_request,
                result
            )


        except Exception as e:

            print(
                f"\n❌ Computer task failed: {e}"
            )

            save_friday_memory(
                user_request,
                f"Computer task failed: {e}"
            )

        return


    # ==================================================
    # WEB
    # ==================================================

    if category == "web":

        try:

            result = run_web_task(
                user_request
            )


            print("\n🌐 FRIDAY:")


            if result.get(
                "success",
                False
            ):

                print(result)

            else:

                print(
                    "❌ Web task failed:"
                )

                print(
                    result.get(
                        "error",
                        "Unknown error"
                    )
                )


            # --------------------------------------
            # Save web task to memory
            # --------------------------------------

            save_friday_memory(
                user_request,
                result
            )


        except Exception as e:

            print(
                f"\n❌ Web task failed: {e}"
            )

            save_friday_memory(
                user_request,
                f"Web task failed: {e}"
            )

        return


    # ==================================================
    # UTILITY TOOLS
    # ==================================================

    if category in [
        "calculator",
        "pdf",
        "file"
    ]:

        try:

            result = run_utility_task(
                user_request
            )


            print("\n🛠️ FRIDAY:")


            if result.get(
                "success",
                False
            ):

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


            # --------------------------------------
            # Save utility task to memory
            # --------------------------------------

            save_friday_memory(
                user_request,
                result
            )


        except Exception as e:

            print(
                f"\n❌ Utility task failed: {e}"
            )

            save_friday_memory(
                user_request,
                f"Utility task failed: {e}"
            )

        return


    # ==================================================
    # NORMAL CONVERSATION
    # ==================================================

    if category == "conversation":

        try:

            answer = normal_conversation(
                user_request
            )


            print("\n🤖 FRIDAY:")
            print(answer)


            # --------------------------------------
            # Save conversation
            # --------------------------------------

            save_friday_memory(
                user_request,
                answer
            )


        except Exception as e:

            print(
                f"\n❌ Conversation error: {e}"
            )

        return


    # ==================================================
    # OTHER TASKS
    # ==================================================

    message = (
        f"{category} system "
        "will be connected in the next lesson."
    )


    print(
        f"\n⚠️ {message}"
    )


    # Save even unsupported requests
    save_friday_memory(
        user_request,
        message
    )


# ==================================================
# MAIN LOOP
# ==================================================

print("\n====================================")
print("          🤖 FRIDAY AI")
print("====================================")

print("Type 'exit' to stop.")


while True:

    user_request = input(
        "\nYou: "
    )


    # ==================================================
    # EXIT
    # ==================================================

    if user_request.lower().strip() == "exit":

        print(
            "\nFRIDAY: Goodbye!"
        )

        break


    # ==================================================
    # EMPTY INPUT
    # ==================================================

    if not user_request.strip():

        continue


    # ==================================================
    # RUN FRIDAY
    # ==================================================

    run_friday(
        user_request
    )