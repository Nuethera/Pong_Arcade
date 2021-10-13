import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        #self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('lime green')
        self.seth(60)

    def move(self):
        if self.ycor() >= 380 or self.ycor() <= -380:
            a = 180 - (2 * (90 - self.heading()))
            self.seth(self.heading() - a)
            self.fd(20)
        self.fd(20)

