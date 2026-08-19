import uuid

from memory import (
    add_message,
    get_recent_memory
)

from long_term_memory import (
    save_memory,
    get_memories
)

from semantic_memory import (
    save_semantic_memory,
    search_semantic_memory
)

from memory_extractor import (
    analyze_memory
)

from context_manager import (
    build_context
)


# ==================================================
# GET MEMORY CONTEXT
# ==================================================

def get_memory_context(
    user_input
):

    # ----------------------------------------------
    # Short-term memory
    # ----------------------------------------------

    recent_messages = get_recent_memory(
        limit=10
    )


    # ----------------------------------------------
    # Long-term memory
    # ----------------------------------------------

    long_term_memories = get_memories(
        limit=10
    )


    # ----------------------------------------------
    # Semantic memory
    # ----------------------------------------------

    semantic_memories = search_semantic_memory(
        user_input,
        n_results=3
    )


    # ----------------------------------------------
    # Build context
    # ----------------------------------------------

    context = build_context(

        recent_messages,

        long_term_memories,

        semantic_memories
    )


    return context


# ==================================================
# SAVE CONVERSATION
# ==================================================

def save_conversation(
    user_input,
    assistant_response
):

    # ----------------------------------------------
    # Short-term memory
    # ----------------------------------------------

    add_message(
        "user",
        user_input
    )

    add_message(
        "assistant",
        assistant_response
    )


    # ----------------------------------------------
    # Long-term memory
    # ----------------------------------------------

    save_memory(
        "user",
        user_input
    )

    save_memory(
        "assistant",
        assistant_response
    )


# ==================================================
# PROCESS IMPORTANT MEMORY
# ==================================================

def process_memory(
    user_input
):

    memory_result = analyze_memory(
        user_input
    )


    # ----------------------------------------------
    # Check if important
    # ----------------------------------------------

    if memory_result.get(
        "remember",
        False
    ):

        memory_id = str(
            uuid.uuid4()
        )


        memory_text = memory_result.get(
            "memory",
            ""
        )


        if memory_text:

            save_semantic_memory(

                memory_id,

                memory_text
            )


            print(
                "💾 Important information remembered."
            )


            return True


    return False


# ==================================================
# COMPLETE MEMORY PROCESS
# ==================================================

def remember_conversation(
    user_input,
    assistant_response
):

    # ----------------------------------------------
    # Save conversation
    # ----------------------------------------------

    save_conversation(

        user_input,

        assistant_response
    )


    # ----------------------------------------------
    # Analyze important memory
    # ----------------------------------------------

    process_memory(
        user_input
    )