from random import choice


lottery_items = (1,2,3,4,5,6,7,8,9,'a','b','c','d','e')

picked_items = []

count = 0
while count <= 4:
    picked_items.append(choice(lottery_items))
    count += 1


print(picked_items)
