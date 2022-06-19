import turtle as t

tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    tim.right(10)


def turn_counterclockwise():
    tim.left(10)


def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forwards)  # recommend using keyword inputs for event listeners
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_counterclockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=clearscreen)

screen.exitonclick()
