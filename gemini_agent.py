from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import uuid

from semantic_memory import (
    save_semantic_memory,
    search_semantic_memory
)

# Short-term memory
from memory import (
    add_message,
    get_recent_memory
)

# Long-term memory
from long_term_memory import (
    create_table,
    save_memory,
    get_memories
)

# Context manager
from context_manager import build_context

# Tools
from tools import (
    add,
    subtract,
    multiply,
    divide
)

from pdf_tool import search_pdf


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
# DATABASE SETUP
# ==================================================

create_table()


# ==================================================
# TOOLS
# ==================================================

tools = [
    add,
    subtract,
    multiply,
    divide,
    search_pdf
]


# ==================================================
# START AGENT
# ==================================================

print("\n================================")
print("       AI AGENT STARTED")
print("================================")

print("Type 'exit' to stop the agent.")


while True:

    # ----------------------------------------------
    # Get user input
    # ----------------------------------------------

    user_input = input("\nYou: ")

    if user_input.lower().strip() == "exit":

        print("\nAI: Goodbye!")

        break

    semantic_memories = search_semantic_memory(
    user_input,
    n_results=3
)
    # ----------------------------------------------
    # Get short-term memory
    # ----------------------------------------------

    recent_messages = get_recent_memory(
        limit=10
    )


    # ----------------------------------------------
    # Get long-term memory
    # ----------------------------------------------

    long_term_memories = get_memories(
        limit=10
    )

    semantic_memories = search_semantic_memory(
    user_input,
    n_results=3
)

    # ----------------------------------------------
    # Build context
    # ----------------------------------------------

    context = build_context(
    recent_messages,
    long_term_memories,
    semantic_memories
)


    # ----------------------------------------------
    # Create prompt
    # ----------------------------------------------

    prompt = f"""
You are a helpful personal AI agent.

You can use the available tools when necessary.

Available tools include:

- Calculator
- PDF search
- Conversation memory


Here is the conversation context:

{context}


Current user request:

{user_input}


Instructions:

1. Use the conversation context when answering
   follow-up questions.

2. Use the calculator tools when calculations
   are required.

3. Use the PDF search tool when the user asks
   about information from the PDF.

4. Do not invent information from the PDF.

5. Answer clearly and naturally.
"""


    # ----------------------------------------------
    # Ask Gemini
    # ----------------------------------------------

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=tools
            )
        )


        answer = response.text


        # ------------------------------------------
        # Save to short-term memory
        # ------------------------------------------

        add_message(
            "user",
            user_input
        )

        add_message(
            "assistant",
            answer
        )


        # ------------------------------------------
        # Save to long-term memory
        # ------------------------------------------

        save_memory(
            "user",
            user_input
        )

        save_memory(
            "assistant",
            answer
        )

        memory_id = f"memory_{len(get_memories(limit=100000)) + 1}"
        memory_id = str(uuid.uuid4())
        save_semantic_memory(
        memory_id,
        user_input
    )

        # ------------------------------------------
        # Display response
        # ------------------------------------------

        print("\nAI:", answer)


    except Exception as e:

        print("\nError:", e)