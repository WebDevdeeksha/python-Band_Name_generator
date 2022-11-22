height = int(input("Enter your height in cms: "))
if(height>120):
    print("You are allowed to have a ride on Roller_Coaster.")
    age = int(input("Enter your age: "))
    if(age<12):
        bill = 8
    elif (age<18):
        bill = 12
    elif (age<21):
        bill = 15
    else:
        bill = 18
    if(input("Do u want ur photo on ticket? Type 'y' or 'n' ? ")=='y'):
        bill += 3
    print(f"Your ticket money is {bill}$")
else:
    print("You are not allowed for Roller_Coaster.")