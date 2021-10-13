from turtle import Turtle


class Player1(Turtle):

    def __init__(self,id):
        super().__init__("square")
        self.speed(0)
        if id == 1:
            self.goto(-580,0)
        elif id == 2:
            self.goto(580,0)
        self.color('white')

        self.up()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        a = self.ycor()
        if a < 330:
            self.sety(a + 20)

    def move_down(self):
        a = self.ycor()
        if a > -325:
            self.sety(a - 20)