from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"score: {self.score} High score:{self.highscore}", True, 'center', ('Courier', 16, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", True, 'center', ('Courier', 16, 'normal'))

    def hit(self):
        self.clear()
        self.score += 1
        self.update_score()
