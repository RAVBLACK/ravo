#Write a python code to read a phone number and email-id from the user and validate it for correctness.

import re
n = input("Enter Mobile Number:")
r = re.fullmatch('[6-9][0-9]{9}',n)
if r!= None:
    print('Valid Number')
else:
    print('Not a Valid Number')

#OUTPUT:
#Enter Mobile Number: 6790967637
#Valid Number
#Enter Mobile Number: 4389185230
#Not a Valid Number
