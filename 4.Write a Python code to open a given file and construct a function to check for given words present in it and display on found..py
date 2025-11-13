#Write a Python code to open a given file and construct a function to check for given words present in it and display on found.


with open('example1.txt',) as file:
    contents = file.read() 
    print(contents)          

    search_word = input("Enter a word you want to search in file: ")
    
    if search_word in contents:  
        print('Word found')
    else:
        print('Word not found')
