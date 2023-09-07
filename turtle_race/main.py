import time
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=630)  # width = twice the xcord + turtle length

guess = screen.textinput(prompt="RED/ GREEN/ BLUE/ PINK/ VIOLET", title="Place your Bet")
color_list = ["RED", "GREEN", "BLUE", "PINK", "VIOLET"]
y_cords = [150, 100, 50, 0, -50]  # diff ycords bc each have diff position in ycord
turtles = []  # empty list for storing turtle objs


for i in range(0, 5):  # defining 4 turtle objects
    tony = Turtle()  # every turtles name will be tony but they'll be diff instances
    tony.shape("turtle")  # changing shape
    tony.color(color_list[i])  # picking corresponding colors from color_list list
    tony.penup()
    tony.goto(-320, y_cords[i])  # going to each ones specific starting point
    turtles.append(tony)  # as each finish all above task they are appended as in order to turtles list


def race():
    while True:  # previously defined here a for loop but no need any way it'll exit and return winner so while
        for racer in turtles:  # iterates in the list of turtle methods that was previously appended
            racer.speed(random.choice([0, 10, 6, 3, 1]))  # random speed for each in each iteration
            racer.fd(random.randint(5, 10))  # random fd steps for each racer in each iteration
            if racer.xcor() >= 280:  # checks each racer xcordinate to determine whether reached check point
                return racer.color()  # returns (PEN COLOR, FILL COLOR)


winner = race()
time.sleep(3)  # To make the screen freeze for 3 secs

tony.home()  # returning turtle to home cords
screen.clear()  # clearing screen

if guess.upper() == winner[0]:
    tony.write(f"YOU WON THE BET,{winner[0]} is the winner", align="center", font=("Arial", 24, "normal"))
else:
    tony.write(f"YOU LOST THE BET, {winner[0]} WON", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()
