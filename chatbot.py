"""
CodeAlpha Internship - Python Programming Task 4: Basic Chatbot
-----------------------------------------------------------------
A simple rule-based chatbot that responds to user input using
if-elif conditions. No external libraries or AI models are used -
every reply is matched against a set of predefined keywords.

Key Concepts Used: if-elif, functions, loops, input/output
"""

import random

# ---------------------------------------------------------------
# Predefined replies. Each key is a keyword/phrase to look for in
# the user's message. Some keywords have multiple possible replies
# so the bot doesn't sound too repetitive.
# ---------------------------------------------------------------
RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey! Good to see you."],
    "hi": ["Hi!", "Hello there!", "Hey! Good to see you."],
    "how are you": ["I'm fine, thanks! How about you?"],
    "your name": ["I'm ChatBot, a simple rule-based assistant."],
    "help": ["I can chat about basic greetings. Try: hello, how are you, "
              "your name, thanks, or bye."],
    "thanks": ["You're welcome!", "Anytime!"],
    "thank you": ["You're welcome!", "Anytime!"],
    "bye": ["Goodbye!", "Bye! Have a great day."],
}

FALLBACK_RESPONSES = [
    "Sorry, I didn't quite get that. Try saying 'help' to see what I can do.",
    "I'm not sure how to respond to that yet.",
]

EXIT_KEYWORDS = ("bye", "goodbye", "exit", "quit")


def get_response(user_input: str) -> str:
    """Return a chatbot reply for a single line of user input."""
    text = user_input.lower().strip()

    # Check each keyword using if-elif style matching.
    for keyword, replies in RESPONSES.items():
        if keyword in text:
            return random.choice(replies)

    # No keyword matched.
    return random.choice(FALLBACK_RESPONSES)


def is_exit(user_input: str) -> bool:
    """Check whether the user wants to end the conversation."""
    text = user_input.lower().strip()
    for word in EXIT_KEYWORDS:
        if word in text:
            return True
    return False


def chat():
    """Main loop: keep chatting until the user says bye/exit/quit."""
    print("ChatBot: Hi! I'm a simple rule-based chatbot.")
    print("ChatBot: Type 'bye' anytime to end the chat.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print("ChatBot: Say something, I'm listening!")
            continue

        if is_exit(user_input):
            print("ChatBot:", get_response(user_input))
            break

        print("ChatBot:", get_response(user_input))


if __name__ == "__main__":
    chat()