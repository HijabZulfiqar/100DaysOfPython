print("Welcome to the tip calculator!!!!")
total_bill=float(input("what wah the total bill?"))
tip=int(input("how much tip would you like to give?10,12 or 15?"))
split_bill=int(input("how many people to split bill in?"))

bill_with_tip=tip/100*total_bill+total_bill
bill_per_person=round(bill_with_tip)/split_bill
print(f"Each person should pay ${bill_per_person}")

