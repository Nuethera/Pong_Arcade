from turtle import Turtle, Screen
from player1 import Player1
from Ball import Ball
screen = Screen()


def screen_setup():
    screen.setup(width=1200, height=800)
    screen.bgcolor("black")
    screen.title("PONG!")
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
screen.listen()
#fix keypress conflicts
screen.onkeypress(key='w', fun=p1.move_up)
screen.onkeypress(key='s', fun=p1.move_down)
screen.onkeypress(key='Up', fun=p2.move_up)
screen.onkeypress(key='Down', fun=p2.move_down)

game_is_on = True

while game_is_on:
    ball.move()

screen.exitonclick()
