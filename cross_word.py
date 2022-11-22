choice1 = input("You're at a CrossWord. Choose 'left' or 'right'.\n")
if(choice1=='left'):
    choice2 = input("Choose 'swim' or 'wait'. \n")
    if(choice2=='wait'):
        choice3 = input("Choose one colour from 'red', 'blue', or 'green'.\n")
        if(choice3=='red'):
            print("Fire Game Over")
        elif(choice3=='blue'):
            print("Won Treasure!")
        elif(choice3=='green'):
            print("Beast Game Over")
        else:
            print("Invalid choice Game Over")
    else:
        print("you choose swim, GAME OVER")
else:
    print("You choose right, GAME OVER")