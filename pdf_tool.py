import chromadb


chroma_client = chromadb.PersistentClient(
    path="./pdf_chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="pdf_knowledge"
)


def search_pdf(question: str) -> str:
    """Search the uploaded PDF for information relevant to the question."""

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    documents = results["documents"][0]

    return "\n\n".join(documents)