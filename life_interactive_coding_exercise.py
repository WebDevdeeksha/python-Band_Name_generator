fixed_age = 90
user_age = int(input("Enter your current age: "))
diff = fixed_age - user_age

remaining_no_of_days = 365 * diff
remaining_no_of_weeks = 52 * diff
remaining_no_of_months = 12 * diff

print(f"You have {remaining_no_of_days} days, {remaining_no_of_weeks} weeks, and {remaining_no_of_months} months left.")
