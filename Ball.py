import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        #self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('lime green')
        #random start
        self.seth(60)

    def move(self):
        if self.ycor() >= 380 or self.ycor() <= -380:
            a = 180 - (2 * (90 - self.heading()))
            self.seth(self.heading() - a)
            self.fd(20)
        self.fd(20)

    def check_bounds(self):
        a = 0
        if self.xcor() >= 600:
            a = 1
            #random angle toward p1
            self.seth(150)
        elif self.xcor() <= -600:
            a = 2
            #random angle toward p2
            self.seth(30)
        if a != 0:
            self.ht()
            self.goto(0,0)
            self.st()
            print(f"a ={a}")



        return a