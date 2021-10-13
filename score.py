from turtle import Turtle


class Score(Turtle):
    def __init__(self, id):
        super().__init__()
        self.up()
        self.ht()
        self.color('white')
        if id == 1:
            self.goto(-50, 360)
        elif id == 2:
            self.goto(50, 360)
        self.p_score = 0
        self.write_score()

    def write_score(self):
        self.write(arg=f"{self.p_score}", move=False, align='center', font=('OCR A Extended', 20, 'bold'))

    def update_score(self):
        self.clear()
        self.p_score += 1
        self.write_score()
