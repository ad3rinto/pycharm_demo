import random

import colorgram
from turtle import Turtle, Screen
import turtle

# colour_list = []
# colors = colorgram.extract("image.png", 30)
# for i in range(len(colors)):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     rgb_col = (r, g, b)
#     colour_list.append(rgb_col)
#
# print(colour_list)

colours = [(238, 236, 234), (230, 226, 228), (34, 108, 167), (223, 229, 235), (227, 233, 230), (112, 163, 211),
           (153, 57, 85), (219, 156, 94), (246, 204, 84), (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97),
           (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143)]

tim = Turtle()
turtle.colormode(255)

for i in range(10):
    tim.pendown()
    tim.color(random.choice(colours))
    tim.begin_fill()
    tim.circle(5)
    tim.end_fill()
    tim.penup()
    tim.forward(30)
    tim.setpos(10, 10)


screen = Screen()
screen.exitonclick()
