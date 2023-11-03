import time
from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.speed = 10

    def car_creation(self, level, level_reached):
        on = 0
        pr_level = level
        if pr_level % 3 == 0 and self.speed > 1:
            if level_reached == 1:
                self.speed = self.speed - 1
        if random.randint(1, self.speed) == 1:
            on = 1
        if on:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            car.goto(300, rand_y)
            self.car_list.append(car)
        return 0

    def car_movement(self):
        for car in self.car_list:
            car.bk(STARTING_MOVE_DISTANCE)
        #remove from car list to avoid memory wastage