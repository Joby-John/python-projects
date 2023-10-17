import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

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
    car_manager.car_creation()
    car_manager.car_movement()
