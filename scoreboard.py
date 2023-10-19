from turtle import Turtle

FONT = ('Arial', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0
        self.goto(position)
        self.paint_score()

    def increase_score(self):
        self.score += 1
        self.paint_score()

    def paint_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, 'center', FONT)
