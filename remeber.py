import json

username = input("what is your name?")

filename = 'username.json'

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remeber you when you back, " + username + " !")

with open(filename) as f_obj:
    contents = json.load(f_obj).title()
    print("Now, welcome back, " + contents + " !")
