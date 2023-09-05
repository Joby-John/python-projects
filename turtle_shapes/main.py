import random
from turtle import Turtle, Screen

color_names = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Cyan", "Gray"]

side = int(input("Enter side of the polygon you want to draw:- "))
tony = Turtle()
rony = Turtle()


def draw(start):
    for j in range(start):
        tony.right(360 / start)
        tony.fd(50)

        rony.left(360 / start)
        rony.fd(50)


for i in range(3, side + 1):
    start = i
    tony.pencolor(random.choice(color_names))
    rony.pencolor(random.choice(color_names))
    draw(start)

Screen().exitonclick()
