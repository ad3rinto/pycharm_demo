import random
from turtle import Turtle, Screen
import turtle

turtle.colormode(255)
# from prettytable import PrettyTable
direction = [0, 90, 180, 270]
tim = Turtle()
tim.color("red")
tim.shape("circle")
# tim.pensize(20)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, g, b)
    return rand_colour


def random_walk(len_of_walk):
    for _ in range(len_of_walk):
        tim.color(random_color())
        tim.forward(35)
        tim.setheading(random.choice(direction))


def draw_spirograph(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading((tim.heading()+size))


draw_spirograph(5)


# random_walk(200)
# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(50)
#         tim.right(angle)
#
#
# for shape_side_number in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_number)

my_screen = Screen()
my_screen.exitonclick()

# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.add_column("Age", [6, 9, 5])
# print(table)
# table.align = "l"
# print(table)
