import random
from turtle import Turtle, Screen

colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

x_cood = -250
y_cood = -180

for i in range(len(colours)):
    racer = colours[i]
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colours[i])
    racer.goto(x=x_cood, y=y_cood)
    y_cood += 50
    racer.speed(random.randint(1, 20))

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win")
screen.exitonclick()
