from name_function import get_formatted_name


print("Enter 'q' to quit.")

while True:
    first = input("\nPlease provide first name: ")
    if first == 'q':
        break
    last = input("\nPlease provide last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted text: {formatted_name}")

