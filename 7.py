#A python program to create a regular expression using the MATCH METHOD() to search for strings starting with ‘m’ and having 3 characters.

import re
words = ["man", "mat", "map", "mad", "moon", "mint", "me"]
pattern = r'^m..$'
for w in words:

    if re.match(pattern, w):
        print("Match found:", w)
    else:
        print("No match:", w)

#OUTPUT:
#Match found: man
#Match found: mat
#Match found: map
#Match found: mad
#No match: moon
#No match: mint
#No match: me
