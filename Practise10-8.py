file_names = ['cats.txt', 'dogs.txt']

def file_write(file_names):
    for file_name in file_names:
        if 'cats' in file_name:
            with open(file_name, 'w') as file_obj:
                cats = 'cat1 cat2 cat3'
                file_obj.write(cats)                
        elif 'dogs' in file_name:
            with open(file_name, 'w') as file_obj:            
                dogs = 'dog1 dog2 dog3'
                file_obj.write(dogs)
        
def file_read(file_names):
    for file_name in file_names:
        try:
            with open(file_name) as file_obj:
                contents = file_obj.read()
        except FileNotFoundError:
            print("Sorry, the file " + file_name + " , you try to find, is not exist!")
        else:
            print(contents)

file_read(file_names)
file_write(file_names)
print("\nNow read!\n")
file_read(file_names)
