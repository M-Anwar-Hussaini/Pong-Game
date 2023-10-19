from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, -300)
        self.color('white')
        self.setheading(90)
        flag = False
        for i in range(-300, 301, 10):
            self.pendown() if flag else self.penup()
            self.forward(20)
            flag = not flag

