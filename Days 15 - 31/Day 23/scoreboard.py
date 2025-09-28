FONT = ("Courier", 24, "normal")
STARTING_SCORE = 0
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.start_score = STARTING_SCORE
        self.penup()
        self.hideturtle()
        self.goto(-277,250)
        self.write(f"Level:{self.start_score}", font=FONT)

    def update_score(self):
        self.clear()
        self.start_score += 1
        self.write(f"Level:{self.start_score}", font=FONT)

    def end_game(self):
        self.goto(-75,0)
        self.write("GAME OVER", font=FONT)