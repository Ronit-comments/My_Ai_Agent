conversation_history = []


def add_message(role, message):
    conversation_history.append({
        "role": role,
        "message": message
    })


def get_memory():
    return conversation_history