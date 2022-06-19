from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 10, "normal")
DATA_FILE = 'data.txt'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.sety(280)
        self.score = 0
        self.get_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_high_score(self):
        with open('data.txt') as data:
            self.high_score = int(data.read())
        
    def update_high_score(self):
        with open('data.txt', mode='w') as data:
            data.write(f"{self.high_score}")

            