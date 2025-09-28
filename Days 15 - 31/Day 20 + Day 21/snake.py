from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        # self.move()

        x_position = 20
        for index in range(3):
            self.segment = Turtle("square")
            self.segment.color("white")
            self.segment.penup()
            self.segment.goto(index * x_position, 0)
            self.segments.append(self.segment)

    def extend(self):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.goto(600, 0)
        self.segments.append(self.segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
            self.segment.heading()

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
            self.segment.heading()

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
            self.segment.heading()

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
            self.segment.heading()
