with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    for line in file_object:
        print(line.rstrip())
# print(contents.rstrip())


with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()


pi_string = ''

# concatenate lines
for line in lines:
    pi_string += line.strip()


print(pi_string)