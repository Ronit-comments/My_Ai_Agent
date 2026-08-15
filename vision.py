from google import genai
from google.genai import types
from dotenv import load_dotenv
from PIL import Image
import os


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_screen():

    image = Image.open("screen.png")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[
            "Describe what is visible on this computer screen. "
            "Focus on applications, buttons, text fields, "
            "menus, and other elements that an automation "
            "agent could interact with.",
            image
        ]
    )

    return response.text