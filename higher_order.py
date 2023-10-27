from turtle import Turtle, Screen

tade = Turtle()
screen = Screen()


def move_forward():
    tade.forward(10)


screen.listen()
screen.onkey(move_forward, "a")
screen.exitonclick()
