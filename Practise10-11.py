import json

def write_number(filename):
    with open(filename, 'w') as f_obj:
        try:
            number = int(input("Tell me your favorite number?"))
        except ValueError:
            print("Please only enter numbers!")        
        else:
            json.dump(number, f_obj)

def read_number(filename):
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except:
        pass
    else:
        print("I know your favorite number is: " + str(number) + " !")
        
        
filename = 'favorite_numbers.json'

write_number(filename)
read_number(filename)
