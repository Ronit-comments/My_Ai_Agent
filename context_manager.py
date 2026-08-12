def build_context(
    recent_messages,
    long_term_memories=None,
    semantic_memories=None
):

    context = ""

    # --------------------------------
    # Recent conversation
    # --------------------------------

    context += "Recent conversation:\n"

    for message in recent_messages:

        context += (
            f"{message['role']}: "
            f"{message['message']}\n"
        )


    # --------------------------------
    # Long-term SQLite memory
    # --------------------------------

    if long_term_memories:

        context += "\nPrevious conversation memories:\n"

        for role, message in long_term_memories:

            context += (
                f"{role}: "
                f"{message}\n"
            )


    # --------------------------------
    # Semantic memory
    # --------------------------------

    if semantic_memories:

        context += "\nRelevant semantic memories:\n"

        for memory in semantic_memories:

            context += f"- {memory}\n"


    return context