import random
import turtle
from turtle import Turtle, Screen

tony = Turtle()

turtle.colormode(255)
tony.speed("fastest")
angle = int(input("Enter the angle with which you want to draw, hint:- smaller = more beautiful:- "))


def spirograph(angle_size):
    for i in range(int(360 / angle_size)):  # bc circle can only be drawn a certain times without overlapping
        tony.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tony.circle(100)
        curr_heading = tony.heading()  # to get the current angle of the turtle
        tony.setheading(curr_heading + angle_size)  # adding 5 degrees to the previous angle


spirograph(angle)

Screen().exitonclick()
