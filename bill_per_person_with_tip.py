bill = float(input("Enter the amount of bill: "))
tip = float(input("Enter the %age of tip: "))
no_of_person = int(input("Enter the number of persons: "))

tip_cal = bill * (tip/100)
new_bill = bill + tip_cal
bill_per_person = round((new_bill/no_of_person),2)
print(f"Bill per person is {bill_per_person} rupees.")
