from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

from memory import add_message, get_memory
from tools import add, subtract, multiply, divide
from pdf_tool import search_pdf


# -------------------------
# Gemini setup
# -------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# -------------------------
# Tools
# -------------------------

tools = [
    add,
    subtract,
    multiply,
    divide,
    search_pdf
]


# -------------------------
# Format memory
# -------------------------

def format_memory(history):

    formatted = ""

    for message in history:
        formatted += (
            f"{message['role']}: "
            f"{message['message']}\n"
        )

    return formatted


# -------------------------
# Agent loop
# -------------------------

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break


    # Save user message
    add_message(
        "user",
        user_input
    )


    # Get conversation memory
    history = get_memory()

    formatted_history = format_memory(history)


    # Create prompt
    prompt = f"""
You are a helpful AI agent.

Here is the conversation history:

{formatted_history}

Use the available tools when necessary.

Current user message:
{user_input}
"""


    # Ask Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=tools
        )
    )


    # Save AI response
    add_message(
        "assistant",
        response.text
    )


    print("\nAI:", response.text)