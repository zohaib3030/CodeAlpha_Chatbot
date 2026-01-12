def chabot():
    print("Welcome to my CHATBOT!")
    print("Type 'bye' to end the conversation..")

#responses
    responses={ "hey":"Hi, I'm there!",
               "how are you":"I'm fine! How can I help you today?",
               "what is your name":"I'm Zohaib's Chatbot!",
               "thanks":"You're Welcome!",
               "bye":"Goodbye!"
    }

    while True:
        user_input=input("You:").lower().strip()

        if user_input in responses:
            print("Chatbot:",responses[user_input])

            if user_input=="bye":
                break
        else:
            print("Sorry, I don't understand that!")  

chabot()              