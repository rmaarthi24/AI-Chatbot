def get_bot_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"

    elif "hi" in user_input:
        return "Hi there!"

    elif "your name" in user_input:
        return "I am a simple AI chatbot."

    elif "how are you" in user_input:
        return "I am fine! Thanks for asking."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand."