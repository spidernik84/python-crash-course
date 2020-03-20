print("Hi, what topping would you like on your pizza?")


while True:
    pizza_topping = input("Topping: ")

    if pizza_topping == 'quit':
        break

    print(f"You chose topping: {pizza_topping}")
