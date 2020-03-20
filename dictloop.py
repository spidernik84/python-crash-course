food = {
    "apple" : "fruit",
    "tiramisu" : "dessert",
    "pasta" : "main",
}


for course, food_type in sorted(food.items()):
    print(f"The {course} is a type of {food_type}")


for course in food.keys():
    print(f"{course.title()} is good for you.")

for food_type in food.values():
    print(f"{food_type.title()} is good for you.")



fav_foods = {
    "erik" : "chocolate",
    "sara" : "pizza",
    "tim" : "sushi",
    "john" : "pizza",
}

print("The mentioned foods are:")
# Set rimuove i duplicati
for food in set(fav_foods.values()):
    print(food)


