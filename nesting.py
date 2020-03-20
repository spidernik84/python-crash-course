# store infos about a pizza being ordered

pizza = {
    "toppings" : ["mushrooms", "tomato", "mozzarella"],
    "crust" : "thick"
}
# summarize

print(f"you ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print(topping)



pets = {
"spike" : {
    "animal" : "dog",
    "age" : 2,
    "owner" : "Jim",
},

"rosie" : {
    "animal": "cat",
    "age": 1,
    "owner": "Priscilla",
}

}

for pet, petdata in pets.items():
    print(f"{pet} is a {petdata['animal']}, is {petdata['age']} years old and is owned by {petdata['owner']}")
