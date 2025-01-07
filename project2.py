print("Welcome to the tip calculator")
bill=float(input("what was the total bill? $"))
tip=int(input("How much tip you want to give?  10,12,or 15?"))
persons=int(input("How many people to split the bill?"))
bill_with_tip = tip/100 *bill + bill
print("each person should pay :$"+ str(bill_with_tip))