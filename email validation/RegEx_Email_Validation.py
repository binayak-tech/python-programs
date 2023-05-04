# CONDITIONS 
# starts with a to z alphabet
# it can contain 0 or 1 (. or _) before @
# numbers [0-9] zero or more occurance
# @ one occurance
# . at position -2 or -3

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

#-----RegEx------
# ^ = starts with
# [a-z] = letter small a to z
# + = joining (one or more occurances)
# [\._] = . and _ present
# ? = zero or one occurances
# [a-z 0-9] a to z and 0 to 9 
# [@]\w = search for @
# [.]\w = search for . 
# {2,3} = in position 2 or 3
# $ ends with ,  {2,3}$ = 2 , 3 position from end 


user_email = input("Enter your Email: ")
if re.search(email_condition,user_email):
    print("Validation Successful")
else:
    print("Wrong Email")