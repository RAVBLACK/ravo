#A python program to create a regular expression to search for strings starting with ‘c’ and having 3 characters using the SEARCH METHOD()?

import re
text="Catch the fish"
pattern=r'\bc..\b'
x=re.search(pattern,text)
if x:
    print("Match found:",x.group())
else:
    print("No match found")

#OUTPUT:
#No match found
    
