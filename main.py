import random
from turtle import Turtle, Screen

# from prettytable import PrettyTable

tim = Turtle()
tim.color("red")
tim.shape("turtle")


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):   
        tim.forward(50)
        tim.right(angle)


for shape_side_number in range(3, 11):
    tim.color(random.choice(["red", "blue", "green"]))
    draw_shape(shape_side_number)

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
