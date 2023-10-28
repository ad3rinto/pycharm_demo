import random
from turtle import Turtle, Screen

colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
x_cood = -250
y_cood = -180
is_race_on = False

for i in range(len(colours)):
    racer = colours[i]
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(colours[i])
    racer.goto(x=x_cood, y=y_cood)
    y_cood += 50
    racer.speed(random.randint(1, 20))
    all_turtles.append(racer)
print(all_turtles)

user_bet = screen.textinput(title="make your bet", prompt="which turtle will win")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've won , the winning colour is {winning_turtle}")
                is_race_on = False
            else:
                print(f"You've lost , the winning colour is {winning_turtle}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
