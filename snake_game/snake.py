from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # the initial coordinates of first 3 squares
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.i = 0
        self.create_snake()  # creating snake by calling create_snake function when instance for the class is created
        # itself
        self.head = self.body[0]  # assigning head only after creating body list 1st bc else there will arise an
        self.tail = self.body[-1]
        # index error.

    def create_snake(self):
        for position in START_POSITION:
            self.grow_body(position)

    def grow_body(self, pos):
        new_seg = Turtle("circle")
        new_seg.color("white")
        new_seg.penup()
        self.body.append(new_seg)
        new_seg.setposition(pos)

    def new_seg(self):
        x = self.body[-1].xcor()
        y = self.body[-1].ycor()
        self.grow_body((x, y))

    def move(self):  # moves much like puzhu last sq 1st move cheyth 2nd
        # nte pos le ethum 2nd 1st nte,last 1st update aavum
        # makes squares follow previous squares, ie 2 follow 1, 1 follow 0
        for body_num in range(len(self.body) - 1, 0, -1):  # start , stop, step
            new_x = self.body[body_num - 1].xcor()  # (2sq goes to 1sq place 1sq goes to heads place)
            new_y = self.body[body_num - 1].ycor()
            self.body[body_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):  # if bc opp direction keystrokes are illegal in snake game
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
