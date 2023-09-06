import random
import turtle
from turtle import Turtle, Screen

tony = Turtle()

turtle.colormode(255)
tony.speed("fastest")
for i in range(100):
    tony.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    tony.circle(100)
    curr_heading = tony.heading()  # to get the current angle of the turtle
    tony.setheading(curr_heading + 5)  # adding 5 degrees to the previous angle

Screen().exitonclick()
