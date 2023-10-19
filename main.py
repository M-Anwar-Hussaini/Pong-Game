import time
from turtle import Screen

from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')

screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
