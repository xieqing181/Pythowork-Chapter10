file_names = ['Alice in wonderland.txt', 'Pride and Prejudice.txt']

for file_name in file_names:
    
    with open(file_name) as file_obj:
        contents = file_obj.read().lower()
        nums = contents.count('the')
        print("The word: 'the' appears: " + str(nums) + 
        " times. In " + file_name.title())
