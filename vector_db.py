import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="my_knowledge"
)

documents = [
    "Python is a high-level programming language known for its simple and readable syntax.",
    "Machine learning is a subset of artificial intelligence that allows computers to learn patterns from data.",
    "Artificial intelligence is the field of computer science concerned with creating systems that can perform tasks that normally require human intelligence."
]

ids = [
    "python_1",
    "ml_1",
    "ai_1"
]

collection.add(
    documents=documents,
    ids=ids
)

print("Documents added successfully!")

results = collection.query(
    query_texts=["What is Python used for?"],
    n_results=2
)

print(results)