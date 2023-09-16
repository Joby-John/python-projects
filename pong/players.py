from turtle import Turtle


class Players:
    def __init__(self):
        self.player_list = []
        self.create_players()

    def create_players(self):

        for i in range(0,2):
            player = Turtle()
            player.color("white")
            player.shape("square")
            player.shapesize(stretch_len=.5, stretch_wid=4, outline=5)
            player.penup()
            self.player_list.append(player)
        self.player_list[0].goto(280, 0)
        self.player_list[1].goto(-280, 0)
