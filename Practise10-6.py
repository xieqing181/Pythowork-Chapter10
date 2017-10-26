def num_add():
    '''def a funcation that can add int, and report error to user if it is not
    int entered'''
    print("Please tell us two numbers, I will reply you the sum.")
    try:
        first_number = int(input("First_number: "))
    except ValueError:
        print("Please only enter numbers, not letters!")
    try:
        second_number = int(input("Second_number: "))
    except ValueError:
        print("Please only enter numbers, not letters!")
    try:
        sum = first_number + second_number
    except UnboundLocalError:
        pass
    else:
        return sum

sum1 = num_add()
print(sum1)
        
