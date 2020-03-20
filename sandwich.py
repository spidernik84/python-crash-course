orders = ["Mediterranean sandwich", "pastrami", "chicken sandwich", "pastrami", "tuna sandwich", "pastrami"]
completed_sandwiches = []


print("We have ran out of pastrami!")

while "pastrami" in orders:
    orders.remove("pastrami")

while orders:
    for sandwich in orders:

        completed_sandwiches.append(orders.pop())
        print(f"I made you a {sandwich}")
    

print("These sandwiches have been made: ")

for completed_sandwich in completed_sandwiches:
    print(completed_sandwich)
