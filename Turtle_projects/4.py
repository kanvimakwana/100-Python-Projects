from turtle import Turtle, Screen
import random

t = Turtle()
t.speed(2)  
t.pensize(5)

colors = ["red", "blue", "yellow", "green", "purple", "indigo", "seagreen",
          "orange", "pink", "slategrey", "beige", "skyblue", "magenta"]

walk = ["forward", "right", "left","back"]

for _ in range(5000):  
    t.color(random.choice(colors))  
    direction = random.choice(walk)  
    step_size = 30
    angle = 90  

    if direction == "forward":
        t.forward(step_size)
    elif direction == "back":
        t.backward(step_size)
    elif direction == "right":
        t.right(angle)
        t.forward(step_size)  
    elif direction == "left":
        t.left(angle)
        t.forward(step_size)  

screen = Screen()
screen.exitonclick()
