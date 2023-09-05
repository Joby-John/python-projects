from turtle import Turtle, Screen

tony = Turtle()
scr = Screen()

tony.shape("triangle")
tony.color("black")


# square
def square():
    tony.forward(100)
    tony.right(90)


for i in range(4):
    square()

# dashed line
tony.penup()
tony.left(180)
tony.forward(500)
tony.right(90)
tony.forward(200)
tony.right(90)


def d_line():  # dashed line
    tony.pendown()
    tony.forward(10)
    tony.penup()
    tony.forward(10)


for i in range(50):
    d_line()

scr.exitonclick()
