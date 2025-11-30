responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm good! How can I help you?",
    "bye": "Goodbye!",
    "name": "I'm a simple chatbot created by Khushi!"
}
print("Chatbot started! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye!")
        break

    # respond if message exists
    response = responses.get(user_input, "Bot: I don't understand that.")
    print("Bot:", response)
