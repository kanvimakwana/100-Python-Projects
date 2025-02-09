#hirst dot painting
hirst_palette = [
    (202, 164, 109),  # Warm Beige
    (238, 226, 189),  # Soft Cream
    (150, 75, 0),     # Rich Brown
    (221, 123, 99),   # Coral Orange
    (53, 100, 60),    # Deep Green
    (13, 72, 74),     # Teal Blue
    (171, 233, 233),  # Light Aqua
    (30, 81, 123),    # Ocean Blue
    (240, 128, 128),  # Light Coral
    (255, 217, 102),  # Soft Yellow
    (179, 57, 81),    # Raspberry Red
    (64, 224, 208),   # Turquoise
    (233, 150, 122),  # Dark Salmon
    (102, 51, 153),   # Deep Purple
    (250, 128, 114),  # Salmon
    (255, 140, 0),    # Dark Orange
    (70, 130, 180),   # Steel Blue
    (205, 92, 92),    # Indian Red
    (144, 238, 144),  # Light Green
    (255, 182, 193)   # Light Pink
]

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.setheading(200)
tim.forward(400)
tim.setheading(0)
tim.speed("fastest")
number = 101

for dot in range(1, number):  
    tim.dot(20,random.choice(hirst_palette))  
    tim.forward(50)
    
    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()