#scribble
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.back(10)
def move_clock():
    tim.right(10)
def move_counter():
    tim.left(10)
def clean():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key= "w",fun =move_forwards)
screen.onkey(key= "s",fun =move_backwards)
screen.onkey(key= "a",fun =move_counter)
screen.onkey(key= "d",fun =move_clock)
screen.onkey(key= "c",fun =clean)
screen.exitonclick()