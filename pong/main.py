from turtle import Turtle, Screen
import time
import players
import ball


# setting up screen
screen = Screen()
screen.screensize(600, 600, "black")
screen.title("PING PONG")
screen.tracer(0)
# setting up the divider in the middle
divider = Turtle()
divider.color("white")
divider.width(10)
divider.penup()
divider.hideturtle()
divider.goto(0, 300)
divider.setheading(270)
divider.pendown()
divider.fd(screen.window_height())

player = players.Players()
screen.update()
screen.tracer(1)
balls = ball.Ball()
screen.exitonclick()
