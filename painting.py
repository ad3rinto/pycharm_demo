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
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(250)
tim.setheading(0)
num_of_dots = 100
tim.speed("fastest")

for dot_counts in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colours))
    tim.penup()
    tim.forward(50)
    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
