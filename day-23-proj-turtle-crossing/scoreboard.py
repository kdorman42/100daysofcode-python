from turtle import Turtle
FONT = ("Courier", 24, "normal")
ENDGAME_FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-250, 250)
        self.write(arg=f"Level: {self.score}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg=f"GAME OVER. Womp womp.", align='center', font=ENDGAME_FONT)