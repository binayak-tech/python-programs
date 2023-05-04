from chart import logo,letters

def cipher(start_text, cipher_direction, shift_amount):
    text = ''
    location = 0
    if cipher_direction == "decode":
        shift_amount *= -1
    for i in start_text:
        if i in letters:
            location = letters.index(i)
            new_location = location + shift_amount 
            while new_location > letters_lenght-1:
                new_location -= letters_lenght
            while new_location < 0:
                new_location += letters_lenght
            text += letters[new_location]
        else:
            text += i 
    print(f"The {cipher_direction}d text is : {text}")


print(logo)
letters_lenght = len(letters)
go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt or \nType 'decode' to decrypt:\n").lower()
    if not direction == "encode" and not direction == "decode":
        print("Invalid input! Try again")
        continue
    print(direction)
    msg = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(cipher_direction=direction, start_text = msg, shift_amount = shift)

    restart = input("Type 'yes' to go again or 'no' to exit.\n").lower()
    if restart == "no":
        go_again = False



