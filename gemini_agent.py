from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from pdf_tool import search_pdf

from tools import add, subtract, multiply, divide


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


tools = [
    add,
    subtract,
    multiply,
    divide,
    search_pdf
]


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_input,
        config=types.GenerateContentConfig(
            tools=tools
        )
    )

    print("Gemini:", response.text)