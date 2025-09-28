from turtle import Turtle


class Names(Turtle):

    def __init__(self, x, y, text):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(text)