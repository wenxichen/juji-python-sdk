from juji_python_sdk import Chatbot
import time

# chatbot = Chatbot("https://juji.ai/pre-chat/67782695-4bee-448a-9dad-964fabe82a41")
chatbot = Chatbot("https://test.juji-inc.com/pre-chat/6784c7cc-d67d-478f-b5a7-14b3b4d8d7bf")

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
time.sleep(10)

messages = participation.get_messages()
print(messages)

print("You: Hello, how are you?")
messages = participation.send_chat_msg("Hello, how are you?")
print(messages) 