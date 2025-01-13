from juji_python_sdk import Chatbot
import time

def handle_message(message: dict):
    print(message)
    # if message["type"] == "normal":
    #     print(f"Juji: {message['text']}")
    # elif message["type"] == "flowinfo":
    #     print(f"Juji is waiting for your response...")

chatbot = Chatbot("https://juji.ai/pre-chat/67782695-4bee-448a-9dad-964fabe82a41")

participation = chatbot.start_chat()
participation.add_message_callback(handle_message)

time.sleep(10)

print("You: Hello, how are you?")
participation.send_chat_msg("Hello, how are you?")

time.sleep(10)

print("You: Bye!")
participation.end()