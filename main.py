import time
from turtle import Screen

from ball import Ball
from line import Line
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
right_scoreboard = Scoreboard((100, 270))
left_scoreboard = Scoreboard((-100, 270))
Line()

ball = Ball()

screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')

screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')
screen.onkey(ball.move, 'space')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    # Detect collision with up and down walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() == 330 or
            ball.distance(left_paddle) < 50 and ball.xcor() == -330):
        ball.bounce_x()

    if ball.xcor() < -400:
        right_scoreboard.increase_score()
        ball.goto(0, 0)
        screen.update()
        time.sleep(1)

    if ball.xcor() > 400:
        left_scoreboard.increase_score()
        ball.goto(0, 0)
        screen.update()
        time.sleep(1)

screen.exitonclick()
