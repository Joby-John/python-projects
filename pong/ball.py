import time
from turtle import Turtle, Screen

screen = Screen()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("slow")
        self.y_steps = 10
        self.x_steps = 10
        self.move_ball()
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_steps
        new_y = self.ycor() + self.y_steps
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.y_steps *= -1

    def bounce_horizontal(self):
        self.x_steps *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_horizontal()
