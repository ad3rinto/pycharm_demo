import turtle
from turtle import Turtle, Screen

tade = Turtle()
screen = Screen()
tade.hideturtle()


def move_right():
    tade.setheading(0)
    tade.forward(10)


def move_left():
    tade.setheading(180)
    tade.forward(10)


def move_upwards():
    tade.setheading(90)
    tade.forward(10)


def move_downwards():
    tade.setheading(270)
    tade.forward(10)


def clear_drawing():
    tade.clear()


screen.listen()
screen.onkey(move_right, "k")
screen.onkey(move_left, "h")
screen.onkey(clear_drawing, "c")
screen.onkey(move_upwards, "u")
screen.onkey(move_downwards, "n")

screen.exitonclick()
