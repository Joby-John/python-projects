import time
from turtle import Turtle, Screen
import ball
from players import Players
from scoreboard import Score

game_is_on = True
score = Score()
speed = [.1, .05, .03, .02]


def divider_make():
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


# setting up screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)  # update is at end of while loop
divider_make()

player = Players()  # both of the paddles are created here not in main
balls = ball.Ball()
while game_is_on:
    balls.move_ball()
    # detecting collision with upper boundary
    if balls.ycor() > 280 or balls.ycor() < -280:
        balls.bounce_vertical()
    # detecting collision with paddles
    if balls.distance(player.player_list[0]) < 50 and balls.xcor() > 350:
        balls.bounce_horizontal()
    elif balls.distance(player.player_list[1]) < 50 and balls.xcor() < -350:
        balls.bounce_horizontal()

    # game reset
    # left side misses
    if balls.xcor() < -360:
        score.r_up()
        balls.ball_reset()
    # right side misses
    elif balls.xcor() > 360:
        score.l_up()
        balls.ball_reset()

    screen.update()
    time.sleep(balls.move_speed)

screen.exitonclick()
