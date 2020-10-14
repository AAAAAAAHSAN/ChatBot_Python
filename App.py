from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])
trainer.train([
    "hello",
    "ahsan",
    "hi",
    "thank you"
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response("san")

print(response)