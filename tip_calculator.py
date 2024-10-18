print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_total = (bill * (tip / 100))
total_bill = tip_total + bill
bill_split = (total_bill / people)
final_per_person = round(bill_split, 2)
print(f"Each person should pay: $ {final_per_person}")