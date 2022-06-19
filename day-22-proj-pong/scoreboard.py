from turtle import Turtle
WINNING_SCORE = 5
LEFT_COLOR = 'pink'
RIGHT_COLOR = 'cyan'

class Scoreboard(Turtle):

    def __init__(self, screen_uicolor, screen_width, screen_height):
        super().__init__()
        self.screen_uicolor = screen_uicolor
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.hideturtle()
        self.draw_line()
        self.penup()
        self.color(self.screen_uicolor)
        self.l_score = 0
        self.r_score = 0
        self.update()

    def draw_line(self):
        dash = Turtle("square")
        dash.color(self.screen_uicolor)
        dash.turtlesize(stretch_wid=0.25, stretch_len=1)
        dash.penup()
        dash.goto(0, -(self.screen_height / 2))
        dash.setheading(90)
        dash.width(5)
        while dash.ycor() < self.screen_height / 2:
            dash.stamp()
            dash.forward(40)

    def increment(self, scoring_side):
        if scoring_side == 'left':
            self.l_score += 1
            self.update()
        elif scoring_side == 'right':
            self.r_score += 1
            self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.pencolor(LEFT_COLOR)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.pencolor(RIGHT_COLOR)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def check_winner(self):
        if self.l_score == WINNING_SCORE:
            self.pencolor(LEFT_COLOR)
            self.home()
            self.write("Game Over. Left player wins!", align="center", font=("Courier", 30, "normal"))
            return False
        elif self.r_score == WINNING_SCORE:
            self.pencolor(RIGHT_COLOR)
            self.home()
            self.write("Game Over. Right player wins!", align="center", font=("Courier", 30, "normal"))
            return False
        else:
            return True

