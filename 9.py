#A python program to create a regular expression to search for strings starting with ‘m’ and having 3 characters using the findall() method

import re
text = "man mat map mad mint moon me mom"
pattern = r'\bm..\b'
matches = re.findall(pattern, text)
if matches:
    print("Matches found:", matches)
else:
    print("No match found")

#OUTPUT:
#Matches found: ['man', 'mat', 'map', 'mad', 'me ', 'mom']
