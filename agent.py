import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("AI Agent started!")
print("Type 'exit' to stop.")

while True:

    user_input = input("\nYou: ")

    if user_input.strip().lower() == "exit":
        print("Agent: Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction="""
            You are an AI DSA tutor.

            Rules:
            1. Explain concepts in simple language.
            2. Give practical examples.
            3. Break difficult concepts into steps.
            4. Explain important parts of code.
            5. Be encouraging to beginners.
            """
        )
    )

    print("\nAgent:", response.text)