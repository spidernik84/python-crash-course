
def table():
    guests = int(input("Hello, how many guests are you? "))

    if guests > 8:
        print("Sorry, you will have to wait!")
    else:
        print("Yes, we have a table! Welcome.")



def multiples():
    input_number = int(input("Hello, please enter a number: "))

    if input_number % 10 == 0:
        print("The number is a multiple of 10.")
    else:
        print("The number is a NOT multiple of 10.")


multiples()