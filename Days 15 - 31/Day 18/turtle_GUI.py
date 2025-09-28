import turtle
from turtle import Turtle, Screen, Shape, register_shape
import random

tim = Turtle()
tim.shape("arrow")
tim.shapesize(0.6)
tim.color("medium violet red")
# tim.teleport(-50,150)

colour_list = ["thistle", "plum", "orchid", "medium orchid", "dark orchid", "dark violet", "blue violet", "dim gray"]
# number_of_sides = 3
#
# while number_of_sides < 11:
#     for _ in range(number_of_sides):
#         angle = 360 / number_of_sides
#         tim.pencolor(colour_list[number_of_sides - 3])
#         tim.forward(100)
#         tim.right(angle)
#     number_of_sides += 1

# def movements():
#     move1 = tim.forward(100)
#     move2 = tim.backward(100)
#     move3 = tim.right(100)
#     move4 = tim.left(100)
#     directions = [move1, move2, move3, move4]


# for _ in range (2):
#     random.choice([tim.forward(50), tim.backward(50)])
#     random.choice([tim.right(90),tim.left(90), tim.right(180), tim.left(180)])
#     #random.choice([tim.forward(50), tim.backward(50)])
#     # tim.right(90),
#     # tim.forward(100),
#     # tim.left(90),
#     # tim.forward(100))
#  # just doing everything. no choice

# numbers = [1,2,3,4]
# tim.pensize(10)
# for _ in range(100):
#     execute = random.choice(numbers)
#     if execute == 1:
#         tim.color(random.choice(colour_list))
#         tim.forward(50)
#     elif execute == 2:
#         tim.color(random.choice(colour_list))
#         tim.backward(50)
#     elif execute == 3:
#         tim.color(random.choice(colour_list))
#         tim.right(90)
#         tim.forward(50)
#     else:
#         tim.color(random.choice(colour_list))
#         tim.left(90)
#         tim.forward(50)

# for _ in range(2,10):
#     tim.pencolor(random.choice(colour_list))
#     tim.forward(100)

tim.speed(0)
for _ in range(1, 201):
    tim.color(random.choice(colour_list))
    tim.circle(190)
    tim.right(360 / 200)

screen = turtle.Screen()
screen.exitonclick()
