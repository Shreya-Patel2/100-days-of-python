from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Score

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

playing_game = True
while playing_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.new_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        playing_game = False
        score.game_over()

    # for segment in snake.segments:
    #     if segment == segments[0]:
    #         pass
    #     elif snake.segments[0].distance(segment) < 10:
    #         playing_game = False
    #         score.game_over()


screen.exitonclick()