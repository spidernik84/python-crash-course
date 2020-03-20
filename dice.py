from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1,self.sides)




dice = Die(10)

print(dice.roll_die())