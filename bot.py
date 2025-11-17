import difflib
import os
import datetime

print("🤖 Welcome to Advanced Mini Chatbot!")
print("Type 'quit' to exit.")


responses = {
    "hi": "Hello! How are you?",
    "hello": "Hi there! 😊",
    "how are you": "I'm just a bot, but I'm fine! How about you?",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "help": "You can say hi, hello, how are you, thanks, bye, or quit to exit."
}


os.makedirs("logs", exist_ok=True)
log_file = "logs/chat_log.txt"

def log_chat(user_msg, bot_msg):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"{time} | You: {user_msg} | Bot: {bot_msg}\n")

while True:
    user_input = input("You: ").lower()
    
    if user_input == "quit":
        print("Bot: Bye! 👋")
        log_chat(user_input, "Bye!")
        break
    
    # fuzzy matching
    best_match = difflib.get_close_matches(user_input, responses.keys(), n=1, cutoff=0.6)
    
    if best_match:
        response = responses[best_match[0]]
    else:
        response = "Sorry, I don't understand that. Type 'help' for options."
    
    print(f"Bot: {response}")
    log_chat(user_input, response)
    
  
    if user_input.startswith("add response:"):
        try:
            _, key, value = user_input.split(":", 2)
            key = key.strip().lower()
            value = value.strip()
            responses[key] = value
            print(f"Bot: Response for '{key}' added!")
        except:
            print("Bot: Invalid format. Use add response: key : value")
