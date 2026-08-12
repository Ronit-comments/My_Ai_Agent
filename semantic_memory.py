import chromadb


# --------------------------------
# ChromaDB setup
# --------------------------------

client = chromadb.PersistentClient(
    path="./memory_chroma_db"
)

collection = client.get_or_create_collection(
    name="agent_memories"
)


# --------------------------------
# Save semantic memory
# --------------------------------

def save_semantic_memory(memory_id, memory):

    collection.upsert(
        ids=[memory_id],
        documents=[memory]
    )


# --------------------------------
# Search semantic memory
# --------------------------------

def search_semantic_memory(query, n_results=3):

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    if not results["documents"]:
        return []

    return results["documents"][0]