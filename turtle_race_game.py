# Making a turtle race game with 6 different colour turtles

import turtle
import random
from turtle import Turtle, Screen

screen = Screen()

colours = ["red", "green", "blue", "yellow", "brown", "orange"]
y_pos = [-150, -90, -30, 30, 90, 150]
all_players = []
user_guess = screen.textinput(title="Make a Guess", prompt="Which colour turtle will win the race? ")
print(user_guess)

for player in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[player])
    tim.penup()
    tim.goto(x=-200, y=y_pos[player])
    all_players.append(tim)

if user_guess in colours:
    is_race_on = True

    while is_race_on:
        for players in all_players:
            if(players.xcor() > 200):
                is_race_on = False
                winning_color = players.pencolor()

                if(winning_color == user_guess):
                    print(f"You win! The colour of the winning turtle is {winning_color}.")
                else:
                    print(f"You lose, the colour of the winning turtle is {winning_color}.")

            rand_distance = random.randint(0,10)
            players.fd(rand_distance)

else:
    is_race_on = False
    print(f"{user_guess} colour turtle is not in the race.")




screen.exitonclick()

