requested_toppings = ["tomato", "mushrooms", "pineapple"]


for topping in requested_toppings:
    if topping == "mushrooms":
        print(f"Sorry, we are out of {topping}")
    else:
        print(f"Adding {topping}")