import time
import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400)
guess = screen.textinput(prompt="RED/ GREEN/ BLUE/ PINK/ VIOLET", title="Place your Bet")
color_list = ["RED", "GREEN", "BLUE", "PINK", "VIOLET"]
y_cords = [150, 100, 50, 0, -50]
turtles = []
for i in range(0, 5):
    tony = Turtle()
    tony.shape("turtle")
    tony.color(color_list[i])
    tony.penup()
    tony.goto(-320, y_cords[i])
    turtles.append(tony)


def race():
    for k in range(0, 150):
        for racer in turtles:
            racer.speed(random.choice([0, 10, 6, 3, 1]))
            racer.fd(random.randint(5, 10))
            if racer.xcor() >= 280:
                return racer.color()


winner = race()
print(winner)
time.sleep(3)
tony.home()
screen.clear()

if guess.lower() == winner[0]:
    tony.write(f"YOU WON THE BET,{winner[0]} is the winner", align="center", font=("Arial", 24, "normal"))
else:
    tony.write(f"YOU LOST THE BET, {winner[0]} WON", align="center", font=("Arial", 24, "normal"))

screen.exitonclick()
