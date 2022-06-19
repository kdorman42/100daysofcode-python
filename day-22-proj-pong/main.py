from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BGCOLOR = 'black'
SCREEN_UICOLOR = 'white'
BALL_COLOR = 'spring green'
ball_speed = 0.1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BGCOLOR)
screen.title("Pong")
screen.tracer(0)

ball = Ball(ball_color=BALL_COLOR, screen_height=SCREEN_HEIGHT)
scoreboard = Scoreboard(screen_uicolor=SCREEN_UICOLOR, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
l_paddle = Paddle(screen_uicolor=SCREEN_UICOLOR, screen_width=SCREEN_WIDTH, paddle_position='l_paddle')
r_paddle = Paddle(screen_uicolor=SCREEN_UICOLOR, screen_width=SCREEN_WIDTH, paddle_position='r_paddle')

screen.listen()
screen.onkey(fun=l_paddle.paddle_up, key='w')
screen.onkey(fun=l_paddle.paddle_down, key='s')
screen.onkey(fun=r_paddle.paddle_up, key='Up')
screen.onkey(fun=r_paddle.paddle_down, key='Down')


game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # Detect top/bottom wall collision
    if ball.ycor() > SCREEN_HEIGHT / 2 - 20 or ball.ycor() < -1 * SCREEN_HEIGHT / 2 + 20:
        ball.bounce(coord='y')

    # Detect right paddle collision
    if ball.xcor() > SCREEN_WIDTH / 2 - 80 and ball.distance(r_paddle) < 50:
        ball.bounce(coord='x')
        ball_speed = ball.increase_speed()
    elif ball.xcor() < -1 * SCREEN_WIDTH / 2 + 80 and ball.distance(l_paddle) < 50:
        ball.bounce(coord='x')
        ball_speed = ball.increase_speed()

    # Detect right paddle out of bounds
    if ball.xcor() > SCREEN_WIDTH / 2 - 10:
        ball.reset_position()
        scoreboard.increment('left')

    # Detect left paddle out of bounds
    if ball.xcor() < -1 * SCREEN_WIDTH / 2 + 10:
        ball.reset_position()
        scoreboard.increment('right')

    # Check endgame
    game_is_on = scoreboard.check_winner()

screen.exitonclick()
