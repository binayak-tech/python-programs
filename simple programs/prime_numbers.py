import math
def get_prime(start_num, end_num):
    if start_num < 1 or end_num < 1:
        return "Invalid Number"
    elif start_num > end_num:
        return "Invalid Range"
    else:
        prime_list=[]
        # print(f"----PRIME NUMBERS BETWEEN {start_num} AND {end_num}----")
        for i in range(start_num,end_num+1):
            prime_count = 0
            for j in range(2,i):
                if i % j == 0:
                    prime_count +=1
            if prime_count == 0:
                # print(i)
                prime_list.append(i)
        return prime_list

# prime_list = get_prime(10,20)
# print(prime_list)

def is_prime(number):
    if number < 1:
        return "Invalid Number"
    elif number == 1:
        return "Prime Number"
    else:
        prime_num = True
        for num in range(2,number):
            if number % num == 0:
                prime_num = False
        
        if prime_num == True:
            return "Prime Number"
        else:
            return "Not a Prime Number"

# print(is_prime(97))