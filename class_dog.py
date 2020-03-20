class Dog:
    """ DOG CLASS """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        print(f"{self.name} is now rolling over.")



my_dog = Dog('willie', 3)

print(f"My dog name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

your_dog = Dog('Lily', 5)

print(f"Your dog name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
