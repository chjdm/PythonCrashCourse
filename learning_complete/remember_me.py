import json


def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            return username
    except FileNotFoundError:
        return None
    else:
        return None


def get_new_username():
    filename = "username.json"
    username = input("Enter your name:")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():

    username = get_stored_username()

    if username:
        check = input("Are you {}?(Y/N)".format(username))
        if check == 'Y' or check == 'y':
            print("Welcome back, {}!".format(username))
        else:
            username = get_new_username()
            print("We'll remember when you came back, {}!".format(username))
    else:
        username = get_new_username()
        print("We'll remember when you came back, {}!".format(username))


greet_user()