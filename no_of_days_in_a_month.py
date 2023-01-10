# WAP to find out no of days in a month in a year or leap year
# function with return

def leap_year(year):
    leap = False
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def no_of_days(year,month):
    month_days = [31,28,31,30,31,30,31,30,31,30,31,30]

    if((leap_year(year)==True) and (month==2)):
        return 29
    return (month_days[month-1])

month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = int(input("Enter the year you want to check: "))
month = int(input("Enter month number: "))

if(month<=12) and (month>=1):
    # print("Invalid Input")
    days = no_of_days(year, month)
    print(f"{month_name[month-1]} has {days} number of days in {year}.")
