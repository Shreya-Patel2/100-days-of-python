STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.teleport(STARTING_POSITION[0], STARTING_POSITION[1])


    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > 250:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)