#A python program to create a regular expression to replace a string with a new string

import re
text = "I like apples. Apples are sweet."
pattern = r'apples'
new_string = 'mangoes'
result = re.sub(pattern, new_string, text, flags=re.IGNORECASE)
print("Original text:", text)
print("After replacement:", result)

#Original text: I like apples. Apples are sweet.
#After replacement: I like mangoes. mangoes are sweet.
