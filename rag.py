import chromadb
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# -----------------------------
# 1. Connect to Gemini
# -----------------------------

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -----------------------------
# 2. Connect to ChromaDB
# -----------------------------

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="my_knowledge"
)

# -----------------------------
# 3. Ask the user a question
# -----------------------------

question = input("Ask a question: ")

# -----------------------------
# 4. Search the vector database
# -----------------------------

results = collection.query(
    query_texts=[question],
    n_results=2
)

# Get retrieved documents
documents = results["documents"][0]

# Combine them into one piece of text
context = "\n\n".join(documents)

print("\nRetrieved information:")
print(context)

# -----------------------------
# 5. Send retrieved information
#    to Gemini
# -----------------------------

prompt = f"""
Answer the user's question using ONLY the information provided below.

Information:
{context}

Question:
{question}

If the information does not contain the answer, say:
"I don't have enough information in my knowledge base."
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print("\nAI:", response.text)