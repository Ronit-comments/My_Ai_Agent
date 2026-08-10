from pypdf import PdfReader
import chromadb
from google import genai
from dotenv import load_dotenv
import os

# -------------------------
# Gemini setup
# -------------------------

load_dotenv()

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -------------------------
# PDF extraction
# -------------------------

pdf_path = "documents/Ml.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"


# -------------------------
# Chunking
# -------------------------

def create_chunks(text, chunk_size=1000, overlap=200):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


chunks = create_chunks(text)

print("Number of chunks:", len(chunks))


# -------------------------
# ChromaDB
# -------------------------

chroma_client = chromadb.PersistentClient(
    path="./pdf_chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="pdf_knowledge"
)


# -------------------------
# Store chunks
# -------------------------

ids = [
    f"chunk_{i}"
    for i in range(len(chunks))
]

collection.add(
    documents=chunks,
    ids=ids
)

print("PDF stored in vector database.")


# -------------------------
# Ask question
# -------------------------

question = input(
    "\nAsk a question about the PDF: "
)


# -------------------------
# Retrieve relevant chunks
# -------------------------

results = collection.query(
    query_texts=[question],
    n_results=3
)

retrieved_chunks = results["documents"][0]


# -------------------------
# Create context
# -------------------------

context = "\n\n".join(
    retrieved_chunks
)


# -------------------------
# Ask Gemini
# -------------------------

prompt = f"""
You are answering questions about a PDF.

Use ONLY the information provided below.

PDF information:
{context}

Question:
{question}

If the answer is not present in the PDF, say:

"I could not find the answer in the PDF."
"""


response = gemini_client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)


print("\nAI:", response.text)