print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip=bill*tip/100
total_bill=(bill+tip)/people
print(f"each person should pay:{round(total_bill,2)}")

