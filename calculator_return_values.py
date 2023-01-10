# Calculator with return values

def add(n1, n2):
    return (n1+n2)
def subtraction(n1, n2):
    return (n1-n2)
def multiply(n1, n2):
    return (n1*n2)
def divide(n1, n2):
    return (n1/n2)
def modulus(n1, n2):
    return (n1%n2)

operations = {"+" : add, "-" : subtraction, "*" : multiply, "/" : divide, "%" : modulus}

def calculator():
    num1 = float(input("Enter 1st value: "))
    end_of_game = True
    for key in operations:
        print(key)

    while end_of_game:
        symbol = input("Choose any one option from menu: ")
        num2 = float(input("Enter 2nd number: "))
        calcautor_function = operations[symbol]
        result = calcautor_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {result} ")

        choice = input("Type 'y' to continue with result or 'c' to exit for a new calculation or to stop type 'n': ")
        if(choice=='y'):
            num1 = result
        elif(choice=='c'):
            end_of_game = False
            calculator()
        else:
            end_of_game = False
            print("Game Stopped!")

calculator()
