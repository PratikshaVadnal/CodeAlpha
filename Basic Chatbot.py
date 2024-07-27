import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
  [
      r"my name is (.*)",
      ["Hello %1, nice to meet you!"]
  ],
  [
      r"what is your name?",
      ["My name is Chatbot. How can I help you today?"]
  ],
  [
      r"how are you?",
      ["I'm doing well, thanks for asking! How are you?"]
  ],
  [
      r"what is the weather like?",
      ["Sorry, I can't access weather information yet. But it's a beautiful day for a chat!"]
  ],
  [
      r"quit",
      ["Thank you for chatting with me. Goodbye!"]
  ],
]

# Create a reflection list for common responses
reflections = {
  "what is your name?": "I'm Chatbot",
  "how are you?": "I'm doing well, thanks for asking!"
}

# Create a chatbot object
chatbot = Chat(pairs, reflections)

# Start interacting with the user
print("Welcome to the Chatbot!")
while True:
  user_input = input("You: ")
  bot_response = chatbot.respond(user_input)
  print("Chatbot:", bot_response)
  
  if bot_response == "Thank you for chatting with me. Goodbye!":
    break