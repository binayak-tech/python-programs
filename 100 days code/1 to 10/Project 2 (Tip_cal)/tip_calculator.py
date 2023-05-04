print("Welcome to the tip calculator.\n")
bill_amount = float(input("What was the total bill? ₹"))
no_of_splits = int(input("How many people to split the bill? "))
tip_percent = float(input("What percentage tip would you like to give? \nbellow 15 % is allowed "))

bill_amount += (bill_amount * (tip_percent/100))
per_head_bill = bill_amount/no_of_splits
# Alternate way
# per_head_bill = bill_amount/no_of_splits
# per_head_tip = (bill_amount * (tip_percent/100))/no_of_splits
# per_head_bill += per_head_tip


#round the final per_head_bill to 2 decimal places

#print("Each person should pay: ₹",round(per_head_bill,2), sep = '')


#round() function returns the exact rounded amount. 
# if the value is 12.666 it will return 12.66 
# but if the value is 12.60 it will return 12.6 despite we told it to return 2 decimal places, 
# therefore we can use format funtion to return exactly 2 decimal places.


per_head_bill = "{0:.2f}".format(per_head_bill)
print("Each person should pay: ₹",per_head_bill, sep = '')