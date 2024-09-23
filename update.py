# Simple Python Chatbot

def chatbot_response(user_input):
    # Define basic responses
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi! How can I assist you?",
        "bye": "Goodbye! Have a nice day.",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm your friendly Python chatbot!"
    }

    # Convert input to lowercase to make the bot case-insensitive
    user_input = user_input.lower()

    # Check if the user input matches one of the keys in the response dictionary
    for key in responses:
        if key in user_input:
            return responses[key]

    # Default response if no match is found
    return "Sorry, I don't understand that. Can you rephrase?"


def main():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Break loop if user types 'bye'
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        # Generate a response
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
