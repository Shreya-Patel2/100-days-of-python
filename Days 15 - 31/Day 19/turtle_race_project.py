from turtle import Turtle, Screen
import random

screen = Screen()

# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def move_left():
#     tim.left(10)
#     #tim.forward(10)
#
# def move_right():
#     tim.right(10)
#     #tim.forward(10)
#
# def clear():
#     tim.reset()
#
# screen.listen()
#
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear)

racing = False
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")
colours = {"red":-120, "orange":-70, "yellow":-20, "green":20, "blue":70, "purple":120}

all_turtles = []
for colour in colours:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colour)
    new_turtle.goto(-230,colours[colour])
    all_turtles.append(new_turtle)

if user_bet:
    racing = True

while racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            racing = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost:( The {winning_colour} was the winner.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()