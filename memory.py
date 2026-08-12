conversation_history = []


def add_message(role, message):

    conversation_history.append({
        "role": role,
        "message": message
    })


def get_memory():

    return conversation_history


def get_recent_memory(limit=10):

    return conversation_history[-limit:]