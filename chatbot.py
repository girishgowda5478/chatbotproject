import pickle
import json
import random

# ---------------- LOAD TRAINED MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- LOAD INTENTS ----------------
with open("intents.json") as file:
    intents = json.load(file)


# ---------------- CHATBOT RESPONSE FUNCTION ----------------
def get_response(user_input, history=None):
    """
    user_input : current user message (string)
    history    : list of previous conversations (context)
    """

    user_input = user_input.lower()

    # ---------------- CONTEXT-AWARE LOGIC ----------------
    if history:
        follow_up_words = ["and", "also", "then", "what about"]

        if any(word in user_input for word in follow_up_words):
            last_bot_reply = history[-1]["bot"].lower()

            # Simple context decision
            if "security" in last_bot_reply or "sql injection" in last_bot_reply:
                return (
                    "Continuing from our security discussion: "
                    "SQL Injection is a code injection attack that allows attackers "
                    "to interfere with database queries."
                )

    # ---------------- NORMAL INTENT CLASSIFICATION ----------------
    X = vectorizer.transform([user_input])
    intent = model.predict(X)[0]

    for intent_data in intents["intents"]:
        if intent_data["tag"] == intent:
            return random.choice(intent_data["responses"])

    # ---------------- FALLBACK ----------------
    return "Sorry, I didn't understand that. Could you please rephrase?"
