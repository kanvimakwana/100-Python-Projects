from turtle import Turtle,Screen
import random

t = Turtle()
Color = ["Red","blue","yellow","green","purple","indigo","seagreen","orange","pink","mint","Slategrey","beign","skyblue","magenta"]

def draw(n):
    angle = 360/n
    for _ in range(n):
        t.forward(100)
        t.right(angle)

for sha in range(3,11):
    t.color(random.choice(Color))
    draw(sha)
    

screen  = Screen()
screen.exitonclick()