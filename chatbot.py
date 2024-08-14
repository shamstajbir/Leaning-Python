
def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input:
        return "Hello! How can I assist you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm functioning as expected. How about you?"
    elif 'what is your name' in user_input:
        return "I am a simple chatbot created to assist you."
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def chatbot():
    print("Chatbot: Hi there! Type 'bye' to exit the chat.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if 'bye' in user_input.lower():
            break

if __name__ == "__main__":
    chatbot()
