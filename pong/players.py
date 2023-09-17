from turtle import Turtle, Screen

screen = Screen()


class Players:
    def __init__(self):
        self.player_list = []
        self.create_players()
        screen.listen()
        screen.onkeypress(self.go_up_pl1, "Up")
        screen.onkeypress(self.go_down_pl1, "Down")
        screen.onkeypress(self.go_up_pl2, "w")
        screen.onkeypress(self.go_down_pl2, "s")

    def create_players(self):
        for i in range(0, 2):
            player = Turtle()
            player.color("white")
            player.shape("square")
            player.shapesize(stretch_len=4, stretch_wid=.5, outline=5)
            player.penup()
            if i == 0:
                player.goto(380, 0)
            else:
                player.goto(-380, 0)
            player.setheading(90)
            self.player_list.append(player)

    def go_up_pl1(self):
        new_y = self.player_list[0].ycor() + 20
        self.player_list[0].goto(self.player_list[0].xcor(), new_y)

    def go_down_pl1(self):
        new_y = self.player_list[0].ycor() - 20
        self.player_list[0].goto(self.player_list[0].xcor(), new_y)

    def go_up_pl2(self):
        new_y = self.player_list[1].ycor() + 20
        self.player_list[1].goto(self.player_list[1].xcor(), new_y)

    def go_down_pl2(self):
        new_y = self.player_list[1].ycor() - 20
        self.player_list[1].goto(self.player_list[1].xcor(), new_y)
