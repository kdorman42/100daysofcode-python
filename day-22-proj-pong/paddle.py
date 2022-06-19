from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, screen_uicolor, screen_width, paddle_position):
        super().__init__()
        self.screen_uicolor = screen_uicolor
        self.screen_width = screen_width
        self.player_ind = paddle_position
        self.shape('square')
        self.color(self.screen_uicolor)
        self.shapesize(stretch_wid=5, stretch_len=1)  # 100 x 20
        self.showturtle()
        self.penup()
        if self.player_ind == 'l_paddle':
            y_sign = -1
        else:
            y_sign = 1
        self.goto(y_sign * self.screen_width / 2 - (y_sign * 50), 0)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

