# Turtle listeners

# import turtle as t
#
# tim = t.Turtle()
# screen = t.Screen()
#
# def move_forwards():
#     tim.forward(10)
#
#
# screen.listen()
# screen.onkey(key='space', fun=move_forwards)  # recommend using keyword inputs for event listeners
#
#
# screen.exitonclick()


# # Functions as Inputs:
# def function_a(something):
#     do this with something
#         then do this
#         finally do this
#
# def function_b():
#     do this
#
# function_a(function_b)

# Higher Order Functions -- a function that can work with other functions
# calculator below is higher order function
# some languages don't allow for this
# useful when need to listen for events and trigger a function

# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 + n2
#
# def multiply(n1, n2):
#     return n1 + n2
#
# def divide(n1, n2):
#     return n1 + n2
#
# def calculator(n1, n2, func):
#     func(n1, n2)
#
# result = calculator(2, 3, divide)
# print(result)


# # Object State and Instances

# Turtle racing!

import turtle as t
import random as r

screen = t.Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = t.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def turtle_setup(t_color, t_startpos):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(t_color)
    new_turtle.penup()
    new_turtle.setpos(t_startpos)
    return new_turtle


y_pos = -100
all_turtles = []

for i in range(len(colors)):
    new_turt = turtle_setup(colors[i], (-200, y_pos))
    y_pos += 30
    all_turtles.append(new_turt)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, the {winning_color} turtle is the winner. You lost.")
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
