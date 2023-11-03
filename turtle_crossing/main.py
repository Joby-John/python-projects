import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 1
level_reached = 0 #for speed increase

screen = Screen()
screen.setup(width=600, height=601)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    level_reached = car_manager.car_creation(level, level_reached)
    car_manager.car_movement()

    # Detect collission
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            screen.title("Game over")
        elif player.ycor() > player.FINISH_LINE_Y:
            level += 1
            level_reached = 1
            player.goto(0, -280)
            screen.title(f"Level:{level}")

screen.exitonclick()
