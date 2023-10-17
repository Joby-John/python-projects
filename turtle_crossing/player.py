from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.game_start()

    def game_start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
        screen.listen()
        screen.onkeypress(self.move, "Up")

    def move(self):
        self.fd(MOVE_DISTANCE)
        if self.ycor() == FINISH_LINE_Y:
            writer = Turtle()
            writer.hideturtle()
            writer.write("You Won!")
            self.goto(STARTING_POSITION)


