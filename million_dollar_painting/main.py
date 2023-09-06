import turtle

import colorgram
import random
import turtle as t

tony = t.Turtle()
t.colormode(255)
t.Screen().screensize(500, 500)

tony.setheading(210)
tony.penup()
tony.hideturtle()
tony.fd(575)
tony.setheading(0)
tony.speed("fastest")


def getting_color(color_list):
    selected_color = random.choice(color_list)  # selects one Color object randomly from the list
    rgb = selected_color.rgb  # separates and stores the rgb tuple which we need
    return rgb


def drawing():
    color_list = colorgram.extract("img.jpg", 12)
    # color_list stores a list of objects of class Color that is inside colorgram
    for row_count in range(16):
        for dot_count in range(25):
            tony.dot(20, getting_color(color_list))  # passing dot size and color returned from getting_color
            tony.fd(40)
        if row_count % 2 == 0:
            tony.left(90)
            tony.fd(40)
            tony.left(90)
        else:
            tony.right(90)
            tony.fd(40)
            tony.right(90)


drawing()

turtle.Screen().exitonclick()
