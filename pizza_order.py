print("Welcome to the Python Pizza Deliveries!")
size = input("Which size u want? 'S', 'M', 'L' ").upper()
add_pepperoni = input("Do u want extra pepperoni in ur pizza. Type 'y' or 'n'? ").lower()
add_olives = input("Do u want extra olives in ur pizza. Type 'y' or 'n'? ").lower()
add_cheese = input("Do u want extra cheese in ur pizza. Type 'y' or 'n'? ").lower()

bill = 0
if(size=='S'):
    bill = 15
elif (size=='M'):
    bill = 20
else:
    bill = 25

if(add_pepperoni=='y'):
    if(size=='S'):
        bill += 2
    else:
        bill += 3

if(add_olives=='y'):
    if(size=='S'):
        bill += 2
    elif(size=='M'):
        bill += 4
    else:
        bill += 5

if(add_cheese=='y'):
    bill += 2

print(f"You final bill is ${bill}")