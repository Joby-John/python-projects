from turtle import Turtle, Screen

tony = Turtle()
scr = Screen()

tony.shape("triangle")
tony.color("wheat")


def square():
    tony.forward(100)
    tony.right(90)


for i in range(4):
    square()

scr.exitonclick()
