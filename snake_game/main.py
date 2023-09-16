import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score

BOUNDARY = [(-300, 310)]

screen = Screen()
screen.screensize(580, 580)
screen.title("MY SNAKE")
screen.bgcolor("black")
screen.tracer(0)  # continuous screen update will be off, and we need to manually update screen using update()

game_is_on = True
snake = Snake()
food = Food()
score_board = Score()

screen.listen()  # this function is used to make screen listen to keystrokes
screen.onkey(snake.up, "Up")  # listens for up arrow key and runs function up
screen.onkey(snake.down, "Down")  # careful while passing function names inside functions we should exclude "()"
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = 0
while game_is_on:
    screen.update()  # this function updates screen manually when ever called
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:  # this function returns distance b/w head and food
        food.new_pos()
        score_board.hit()
        snake.new_seg()

    # detect collision with wall
    if (snake.head.xcor() > BOUNDARY[0][1] or snake.head.xcor() < BOUNDARY[0][0] or
            snake.head.ycor() < BOUNDARY[0][0] or snake.head.ycor() > BOUNDARY[0][1]):
        game_is_on = False
        score_board.game_over()

    # detect collision with tail
    for segment in snake.body[1:]:  # sliced bc the head will always have distance from head <10
        if snake.head.distance(segment) < 10:  # if snake hits with any segment of body
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
