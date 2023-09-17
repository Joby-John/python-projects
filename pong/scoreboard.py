from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f"SCORE: {self.lscore}", True, 'center', ('courier', 20, 'normal'))
        self.goto(100, 200)
        self.write(f"SCORE: {self.rscore}", True, 'center', ('courier', 20, 'normal'))

    def l_up(self):
        self.lscore += 1
        self.clear()
        self.update_scoreboard()

    def r_up(self):
        self.rscore += 1
        self.clear()
        self.update_scoreboard()