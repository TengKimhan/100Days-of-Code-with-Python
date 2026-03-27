print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15?"))
people_to_split = int(input("How many people to split the bill?"))

each_person_pay = (bill + bill * tip_percent / 100) / people_to_split

print(f"Each person should pay: ${round(each_person_pay, 2)}")
