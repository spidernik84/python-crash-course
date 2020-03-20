prompt = "Tell me something, I will repeat it back!"
prompt += "\nType 'quit' to make me stop."


active = True

while active:
    user_input = input(prompt)
    if user_input == 'quit':
        active = False
    else:
        print(user_input)

