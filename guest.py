file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
    while True:
        '''ask usr to enter name, print hello, and ask if continue or not'''
        user_name = input("Please enter your name: ")
        file_object.write(user_name.upper() + "\n")
        print("Willkommen, " + user_name.upper() + " !\n")
        if input("To continue, please enter \'next\'.").lower() == 'next':
            continue
        else:
            break

        
        
    

