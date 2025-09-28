print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_tip = 1+(tip/100)
total_bill = bill*total_tip
amount = total_bill/people

amount = format(amount,".5f")

print (f"Each person should pay ${amount}")