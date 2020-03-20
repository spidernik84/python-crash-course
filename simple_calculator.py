print("Welcome to simple calculator.")

def take_digit():
    input_ok = True
    while input_ok:
        try:
            digit = input("Provide an integer:")
            sanitized_result = int(digit)
            return sanitized_result
            input_ok = True
        except ValueError:
            print("Have you provided an integer?")
            input_ok = False


first_digit = take_digit()
second_digit = take_digit()

print(first_digit+second_digit)
