from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("silver")
screen.title("Ping Pong")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

playing = True
while playing:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.home()
        ball.move_speed = 0.01
        ball.bounce_paddle()
        score.l_point()

    if ball.xcor() < -380:
        ball.move_speed = 0.01
        ball.home()
        ball.bounce_paddle()
        score.r_point()

screen.exitonclick()
