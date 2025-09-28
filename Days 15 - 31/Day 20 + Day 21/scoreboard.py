import turtle
from turtle import Turtle


class Score:

    def __init__(self):
        self.score = Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0,270)
        self.score.write("Score = ", False, align="center", font=("Courier",18,"normal"))
        self.updated_score = 0
        self.current_score = Turtle()

    def new_score(self):
        self.updated_score += 1
        self.current_score.color("white")
        self.current_score.penup()
        self.current_score.hideturtle()
        self.current_score.goto(60,270)
        self.current_score.write(f"{self.updated_score}", False, align="center", font=("Courier",18,"normal"))

    def clear(self):
        self.current_score.clear()

    def game_over(self):
        self.score.goto(0,0)
        self.score.write("GAME OVER", False, align="center", font=("Courier",18,"normal"))