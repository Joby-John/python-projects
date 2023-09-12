import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.screensize(600, 600)
screen.title("MY SNAKE")
screen.bgcolor("black")
screen.tracer(0)  # continuous screen update will be off, and we need to manually update screen using update()

game_is_on = True
snake = Snake()
screen.listen()  # this function is used to make screen listen to keystrokes
screen.onkey(snake.up, "Up")  # listens for up arrow key and runs function up
screen.onkey(snake.down, "Down")  # careful while passing function names inside functions we should exclude "()"
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()  # this function updates screen manually when ever called
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
