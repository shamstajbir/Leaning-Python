import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! What's up?"]),
    (r"how are you?", ["I'm doing great, thank you! How about you?", "I'm fantastic! How are you?"]),
    (r"what's your name?", ["I'm your friendly chatbot. What can I call you?", "You can call me Chatbot. How can I help you?"]),
    (r"my name is (.*)", ["Nice to meet you, %1! How can I assist you today?"]),
    (r"how can you help me?", ["I can chat with you and answer your questions. What would you like to talk about?"]),
    (r"thank you|thanks", ["You're welcome!", "No problem at all!"]),
    (r"(.*)", ["Sorry, I didn't understand that. Can you rephrase?", "Hmm, could you tell me more about that?"]),
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chat():
    print("Hi! I'm here to chat with you. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
