import json

def get_stored_username():
    '''if stored username, then use it'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user(new_user):
        #username = input("Sorry, you are new! what's your name?")
        print("Sorry, you are new here, give me a minute to save you in the list!")
        username = new_user
        filename = 'username.json'
        with open(filename, 'a') as f_obj:
            json.dump(username, f_obj)
        return username

def greet_user():
    '''greet user, and specify the name'''
    '''add user check, if it's a new user, ask name first'''
    username_1 = input("Please tell us your name first?").lower()
    username_2 = get_stored_username().lower()
    if username_1 == username_2:
        print("Welcome back, " + username_2.title() + " !")
    else:
        #return username_1
        username_new = get_new_user(username_1)
        print("We'll remeber you when you back, " + username_new + " !")
            
greet_user()
