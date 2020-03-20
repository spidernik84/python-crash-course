# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Are you dividing by zero?")

print("Give two numbers, I'll divide the first by the second.")
print("Enter 'q' to quit.")


while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_num) / int(second_number)
    except ZeroDivisionError:
        print("Are you dividing by zero?")
    else:
        print(answer)

filename = 'asd.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"File {filename} missing...")
