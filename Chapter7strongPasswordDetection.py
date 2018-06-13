#! python3
# strongPasswordDetection - Checks if password strong enough.

import re

# At least eight characters long

eightCharRegex = re.compile(r'(.{8,})')


#Contains both uppercase and lowercase characters and one digit

#upperlowerRegex = re.compile(r'(.*[a-z].*)(.*[A-Z].*)(.*[0-9].*)')
upperlowerRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+')

#Input password
print("Enter your password: ")
mypassword = input()
password = mypassword 
validlongPasswords = []
#for password in eightCharRegex.findall(password) and password in upperlowerRegex.findall(password): 
#    print(password)    
if password not in eightCharRegex.findall(password):
    print('Password too short')
elif password not in upperlowerRegex.findall(password):
    print('Password not secure enough')
else:
    print(str(password) + " is a strong password")
