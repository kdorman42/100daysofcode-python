from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, ball_color, screen_height):
        super().__init__()
        self.color(ball_color)
        self.shape("circle")
        self.penup()
        self.showturtle()
        self.goto(0, 0)
        self.screen_height = screen_height
        self.y_direction = random.choice([-1, 1])
        self.x_direction = random.choice([-1, 1])
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_direction * 10
        new_y = self.ycor() + self.y_direction * 10
        self.goto(new_x, new_y)

    def bounce(self, coord):
        if coord == 'y':
            self.y_direction *= -1
        if coord == 'x':
            self.x_direction *= -1

    def reset_position(self):
        self.home()
        self.y_direction = random.choice([1, -1])
        self.x_direction *= -1
        self.move_speed = 0.1

    def increase_speed(self):
        self.move_speed *= 0.9
        return self.move_speed
