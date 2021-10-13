from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        #self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color('lime green')
        self.seth(80)

    def move(self):
        self.fd(20)

