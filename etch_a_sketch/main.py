from turtle import Turtle, Screen

tony = Turtle()
screen = Screen()
print(tony.pos())


def move_front():
    tony.fd(10)


def move_back():
    tony.back(10)


def move_right():
    tony.right(10)


def move_left():
    tony.left(10)


def clear():
    tony.clear()
    tony.penup()
    tony.home()
    tony.pendown()


screen.listen()
screen.onkey(fun=move_front, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
