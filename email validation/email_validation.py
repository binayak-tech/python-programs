email = input("Enter email address : ")
# constrains -- a@a.in
k,l,n = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-3] == ".") ^ (email[-4] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha:
                        if i == i.upper():
                            l == 1
                    elif i.isdigit():
                        continue
                    elif (i == "_") or (i == ".") or (i == "@"):
                        continue
                    else:
                        n == 1
                if k == 1 or l == 1 or n == 1:
                    print("Invalid email 5")
                else: 
                    print("Email validation successfull")
            else:
                print("Invalid email 4")
        else:
            print("Invalid email 3") 
    else:
        print("Invalid email 2")
else:
    print("Invalid email 1")