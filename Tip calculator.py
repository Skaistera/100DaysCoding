print("Welcome to the tip calculator!")
bill =float(input("What was the total bill? "))
tips = int(input("How much tip would you like to give? "))
people = int(input("How many people to split the bill? "))
bill_with_tips = tips /100 * bill + bill
bill_per_person = bill_with_tips / people
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}" )
