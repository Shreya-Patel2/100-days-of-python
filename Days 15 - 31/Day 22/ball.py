from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_cor = 1
        self.y_cor = 1
        self.move_speed = 0.01

    def move(self):
        new_x = self.x_cor
        new_y = self.y_cor
        self.goto(self.xcor() + new_x, self.ycor() + new_y)

    def bounce_wall(self):
        self.y_cor *= -1

    def bounce_paddle(self):
        self.x_cor *= -1
        self.move_speed *= 0.75
