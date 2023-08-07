import random

game_continue = True

cc_list = ["ROCK", "PAPER", "SCISSOR"]
cc_choice = random.choice(cc_list)
print(f"Computer's random choice is: {cc_choice}")

print("Choose any one option from given menu; ")
menu = ["ROCK", "PAPER", "SCISSOR"]
print(menu)

while game_continue:
    user_choice = input("Enter your choice: ").upper()
    if user_choice not in menu:
        game_continue = False
        print("Not present in Menu")

    elif (user_choice=="ROCK"):
        if(cc_choice=="ROCK"):
            print(f"Computer's random choice is: {cc_choice}")
            print("Since, it's a draw")
        elif(cc_choice=="PAPER"):
            print(f"Computer's random choice is: {cc_choice}")
            print("computer wins!, You lose")
        else:
            print(f"Computer's random choice is: {cc_choice}")
            print("You win!, computer Loses")

    elif(user_choice=="PAPER"):
        if(cc_choice=="ROCK"):
            print(f"Computer's random choice is: {cc_choice}")
            print("You wins!, computer loses")
        elif(cc_choice=="PAPER"):
            print(f"Computer's random choice is: {cc_choice}")
            print("Since, It's a draw")
        else:
            print(f"Computer's random choice is: {cc_choice}")
            print("Computer wins!, You loses")

    else:
        if(cc_choice=="ROCK"):
            print(f"Computer's random choice is: {cc_choice}")
            print("Computer wins!, You lose")
        elif(cc_choice=="PAPER"):
            print(f"Computer's random choice is: {cc_choice}")
            print("You wins!, Computer loses")
        else:
            print(f"Computer's random choice is: {cc_choice}")
            print("Since, It's a draw")
    
    choice = input("\n do you want to play more, type 'y' or 'n': ").lower()
    if(choice=='y'):
        game_continue = True
    elif(choice=='n'):
        game_continue = False
        print("You choses no to play")
    else:
        game_continue = False
        print("You entered an invalid input.")
        
    
