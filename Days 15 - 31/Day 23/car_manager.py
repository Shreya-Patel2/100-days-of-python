COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.y_pos = int(random.randint(-250, 250))
            new_car.goto(300, new_car.y_pos)
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_across(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
