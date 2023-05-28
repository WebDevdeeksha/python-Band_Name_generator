# Making Hirst Project

import random
import turtle
from turtle import Turtle, Screen

screen = Screen()

turtle.up()
turtle.colormode(255)
turtle.speed("fastest")

rgb_colors = [(0,0,0), (255, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (128, 0, 0), (0, 128, 128), (124, 252, 0)]
turtle.setpos(-150, -150)
    
for line_count in range(1,101):
    turtle.dot(20, random.choice(rgb_colors))
    turtle.fd(50)
    
    if line_count%10==0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.fd(500)
        turtle.setheading(0)

turtle.hideturtle()

screen.exitonclick()
