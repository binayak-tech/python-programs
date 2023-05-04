from random import choice,shuffle,sample
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
'u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','?']

password_list = []
s = int(input("How many letters you want in your password: "))
password_list += sample(letters, s)
u = int(input("How many numbers you want in your password: "))
password_list += sample(numbers, u)
v = int(input("How many symbols you want in your password: "))
password_list += sample(symbols, v)

# ANOTHER WAY(unefficient because of multiple loops increasing time complexity)

# password_list = []
# for i in range(s):
#     letter = choice(letters)
#     password_list.append(letter)
    
# for i in range(u):
#     number = choice(numbers)
#     password_list.append(number)

# for i in range(v):
#     symbol = choice(symbols)
#     password_list.append(symbol)

shuffle(password_list)

password = ''
for pw in password_list:
    password += pw

print(f"Your new {len(password)} digits password is: {password}")