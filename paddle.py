from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.default = self.goto(350,0)
        self.shapesize(stretch_wid=5, stretch_len=1)


    def up(self):
        up = self.ycor() + 20
        self.goto(350, up)
        print("niggers")
    def down(self):
        down = self.ycor() - 20
        self.goto(350, down)