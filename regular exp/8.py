#A python program to create a regular expression using the match method() to se

import re
words = ["moon", "mint", "mark", "man", "mice", "mainly", "mood"]
pattern=r'^m...$'
for w in words:
    if re.match(pattern,w):
        print("Match found:",w)
    else:
        print("No match:",w)

#Match found: moon
#Match found: mint
#Match found: mark
#No match: man
#Match found: mice
#No match: mainly
#Match found: mood
