def message_printer(messages):
    """takes a list and prints each message"""

    while messages:
        message = messages.pop()

        sent_messages.append(message)


        print(message)


def message_(parameter_list):
    pass
            

sent_messages = []
messages = ["Hello", "how are you", "I love cats"]

message_printer(messages)

print("Sent:")
print(sent_messages)
print("original list:")
print(messages)