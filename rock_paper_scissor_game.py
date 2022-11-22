import random

MENU = ("""
    1. ROCK
    2. PAPER
    3. SCISSOR""")

print(MENU)

user = int(input("Enter ur choice from 1, 2, and 3:- "))
com_list = ["ROCK","PAPER", "SCISSOR"]
com_choice = random.choice(com_list)
print("computer choice is ", com_choice)

if(user==1):
    if(com_choice=="ROCK"):
        print("IT'S A TIE")
    elif(com_choice=="PAPER"):
        print("YOU LOSE")
    else:
        print("YOU WON!")
elif(user==2):
    if(com_choice=="ROCK"):
        print("YOU WON!")
    elif(com_choice=="PAPER"):
        print("IT'S A TIE")
    else:
        print("YOU LOSE")
elif(user==3):
    if(com_choice=="ROCK"):
        print("YOU LOSE")
    elif(com_choice=="PAPER"):
        print("YOU WON!")
    else:
        print("IT'S A TIE")
else:
    print("INVALID INPUT")