from turtle import Turtle

MOVE_DISTANCE = 50


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape('square')
        self.color('white')
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
