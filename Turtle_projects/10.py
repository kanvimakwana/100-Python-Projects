#turtle race
from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500,height=400)
user = screen.textinput(title="Make your bet", prompt="Which turtle will win the race: Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_pos =[-100, -60, -20, 20, 60, 100]
all = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x= -230,y= y_pos[turtle_index])
    all.append(tim)

if user:
    is_on = True

while is_on:
    for turtle in all:
        if turtle.xcor ()>230:
            is_on = False
            win = turtle.pencolor()
            if win == user:
                print("You've won! The {win} turtle is winner !")
            else:
                print("You've lost! The {win} turtle is winner !")
        dist= random.randint(0,10)
        turtle.forward(dist)
        

screen.exitonclick()