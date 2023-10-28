from turtle import Turtle, Screen

tim = Turtle()
tim.penup()
tim.color("red")
tim.shape("turtle")
tim.goto(x=-230, y=-50)

taj = Turtle()
taj.penup()
taj.color("yellow")
taj.shape("turtle")
taj.goto(x=-230, y=50)

tom = Turtle()
tom.penup()
tom.color("blue")
tom.shape("turtle")
tom.goto(x=-230, y= 0)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win")
screen.exitonclick()
