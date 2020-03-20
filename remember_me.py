import json

def get_stored_username():
    """ Get user if available """
    filename = 'rememberme.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def ask_username():
    username = input("what is your name? ")
    filename = 'rememberme.json'
    with open(filename, 'w') as f:
        json.dump(username,f)
    return username


def greet_user():
    
    username = get_stored_username()
    if username:
        print(f"Hello {username}!")
    else:
        username = ask_username()
        print(f"We will remember you when you come back, {username}!")

greet_user()
