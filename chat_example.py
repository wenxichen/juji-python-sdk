from juji_python_sdk import Chatbot
import time
import dotenv   
import os
dotenv.load_dotenv()

# Create a chatbot instance
chatbot = Chatbot(os.getenv("CHATBOT_URL"))

participation = chatbot.start_chat()


# ########################################################
# # Asynchronous message handling
# ########################################################
# def handle_message(message: dict):
#     if message["type"] == "normal":
#         print(f"Juji: {message['text']}")
#     elif message["type"] == "flowinfo":
#         print(f"Juji is waiting for your response...")

# participation.add_message_callback(handle_message)

# time.sleep(10)

# print("You: Hello, how are you?")
# participation.send_chat_msg("Hello, how are you?")

# time.sleep(10)

# print("You: Bye!")
# participation.end()

########################################################
# Synchronous message handling
########################################################

messages = participation.get_messages()
print(messages)

print("You: Hello, how are you?")
messages = participation.send_chat_msg("Hello, how are you?")
print(messages) 