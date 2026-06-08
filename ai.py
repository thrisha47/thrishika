print("welcome to AI CHATBOT")
print("Type 'exit' anytime to stop the Chatbot.\n")
while True:
    user_input =  input("You: ").lower()
    if user_input=="hello" or user_input =="hi":
        print("Bot: Hello!welcome to DecodeLabs AI Chatbot.")
    elif user_input == "good evening":
        print("Bot: Good Evening! How can I help you?")
    elif user_input == "what's your name":
        print("Bot: I am a Rule-Based AI Chatbot.")
    elif user_input == "what is ai":
        print("Bot: ai means Artificial Intelligence.")   
    elif user_input == "which programming language":
        print("Bot: python.")
    elif user_input == "what is chatbot":
        print("Bot: A chtabot is a program that can communicate with users through text or voice.")
    elif user_input == "help":
        print("Bot: you can ask me about AI,python.")
    elif user_input == "thank you":
        print("Bot: you're welcome!")
    elif user_input == "exit" or user_input =="bye":
        print("Bot: Thank you for using the AI Chatbot.bye")
        break
    else:
        print("Bot: Sorry, I don't understand that.please try another question.")
