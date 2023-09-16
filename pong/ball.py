import time
from turtle import Turtle, Screen


class Ball:
    def __init__(self):
        self.game_is_on = True
        self.boundary = [-300, 300]
        self.angles = [0, 90, 270, 360]
        self.create_ball()

    def create_ball(self):
        ball = Turtle()
        screen = Screen()
        ball.color("white")
        ball.shape("circle")
        ball.penup()
        ball.speed("slow")
        while self.game_is_on:
            screen.tracer(0)
            ball.fd(10)
            if ball.xcor() == -300 or ball.xcor()==300 or ball.ycor()==300 or ball.ycor()==-300:
                ball.setheading(90+ball.heading())
            time.sleep(.1)
            screen.update()
