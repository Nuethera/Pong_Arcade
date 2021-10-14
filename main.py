import time
from turtle import Turtle, Screen
from player1 import Player1
from Ball import Ball
from score import Score

screen = Screen()


def screen_setup():
    screen.setup(width=1200, height=800)
    screen.bgcolor("black")
    screen.title("PONG!")
    screen.tracer(0)
    screen_turtle = Turtle()
    screen_turtle.color('white')
    screen_turtle.speed(0)
    screen_turtle.up()
    screen_turtle.ht()
    screen_turtle.width(5)
    screen_turtle.goto(0, -380)
    screen_turtle.seth(90)
    for i in range(40):
        screen_turtle.down()
        screen_turtle.fd(20)
        screen_turtle.up()
        screen_turtle.fd(20)


screen_setup()
p1 = Player1(id=1)
p2 = Player1(id=2)
ball = Ball()
s1 = Score(id=1)
s2 = Score(id=2)
screen.listen()
# fix keypress conflicts
screen.onkeypress(key='w', fun=p1.move_up)
screen.onkeypress(key='s', fun=p1.move_down)
screen.onkeypress(key='Up', fun=p2.move_up)
screen.onkeypress(key='Down', fun=p2.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move()
    c = ball.check_bounds()

    if c == 1:
        s1.update_score()
    elif c == 2:
        s2.update_score()

    if ball.distance(p2) < 40 and ball.xcor() > 350:
        ball.bounce_x()

    if ball.distance(p1) < 50 and ball.xcor() < -350:
        ball.bounce_x()

screen.exitonclick()
