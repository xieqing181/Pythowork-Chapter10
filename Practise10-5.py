file_name = 'why_programming.txt'

with open(file_name, 'w') as file_object:
    while True:
        user_reason = input("Please spcify why you love python?").upper()
        file_object.write(user_reason + "\n")
        if input("To continue, please enter \'next\': ").lower() == 'next':
            continue
        else:
            break

        
