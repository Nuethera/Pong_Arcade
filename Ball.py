import random
import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        self.color('lime green')
        self.seth(random.randint(-50, 50))

    def move(self):
        if self.ycor() >= 380 or self.ycor() <= -380:
            self.bounce_y()
        self.fd(20)

    def bounce_y(self):
        h = self.heading()
        a = 180 - (2 * (90 - h))
        self.seth(h - a)
        self.fd(20)

    def check_bounds(self):
        a = 0
        if self.xcor() >= 600:
            a = 1
            self.seth(random.randint(130, 230))
        elif self.xcor() <= -600:
            a = 2
            self.seth(random.randint(-50, 50))

        if a != 0:
            self.ht()
            self.goto(0, 0)
            self.st()
            time.sleep(1)

        return a
