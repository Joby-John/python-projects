from turtle import Turtle, Screen
import random

steps = int(input("Enter the steps you want to take:- "))
tony = Turtle()
tony.width(10)
tony.speed(2)
Screen().setup(600, 600)
color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Cyan", "Gray", "Black", "White",
               "Indigo", "Magenta", "Lavender", "Teal", "Maroon", "Turquoise", "Gold", "Silver"]

for i in range(1, steps + 1):
    angle = random.choice([90, 180, 270, 360])
    color = random.choice(color_names)
    tony.color(color)
    tony.setheading(angle)
    tony.forward(20)

Screen().exitonclick()
