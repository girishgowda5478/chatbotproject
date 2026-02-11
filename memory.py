# In-memory conversation storage

chat_memory = {}

def save_message(username, message, reply):
    if username not in chat_memory:
        chat_memory[username] = []

    chat_memory[username].append({
        "user": message,
        "bot": reply
    })

    # Keep only last 5 messages
    chat_memory[username] = chat_memory[username][-5:]


def get_history(username):
    return chat_memory.get(username, [])
