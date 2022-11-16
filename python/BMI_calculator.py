# BMI = weight(kg)/height**2(meter)

height = float(input("enter height in meters: "))
weight = float(input("Enter weight in kgs: "))
BMI = weight/(height**2)
BMI = round(BMI)

if(BMI < 18.5):
    print(f"Your BMI is {BMI} and you are Underweight.")
elif (BMI < 25):
    print(f"Your BMI is {BMI} and you have a Normal Weight.")
elif (BMI < 30):
    print(f"Your BMI is {BMI} and you are slightly Overweight.")
elif (BMI < 35):
    print(f"Your BMI is {BMI} and you are Obese.")
else:
    print(f"Your BMI is {BMI} and you are Clinically Obese.")