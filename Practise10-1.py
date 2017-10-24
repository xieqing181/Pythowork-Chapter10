file_name = 'learning_python.txt'

with open(file_name) as file_object:
    #contents = file_object.read()
    lines = file_object.readlines()
    contents = ''
    for line in lines:
        contents += line
    new_contents = contents.replace('Python', 'C++')
        
    
#print(contents.strip())
print(contents)
print("\nNow print new contents: ")
print(new_contents)
