from semantic_memory import (
    search_semantic_memory,
    delete_semantic_memory
)


def forget_memory(query):

    memories = search_semantic_memory(
        query,
        n_results=1
    )

    if not memories:

        return "I could not find a matching memory."

    memory = memories[0]

    delete_semantic_memory(
        memory["id"]
    )

    return (
        f"Forgotten memory: "
        f"{memory['memory']}"
    )