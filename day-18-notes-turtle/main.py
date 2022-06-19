# import turtle
# from turtle import *  # shorter but not best practice - lose context without module
# if not using a function much, use just import, not from, so you have context
# import turtle as t  # t is an alias for turtle module


# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("medium aquamarine")
# # tkinter allows you to create a GUI
# # turtle relies on tkinter under the hood
#
# for i in range(1, 5):
#     tim.forward(100)
#     tim.right(90)
# screen = Screen()
# screen.exitonclick()

# turtle is packaged with python standard library - small subset of core modules
# pyPI to install other packages not in the standard library

# import heroes  # not in default - pycharm will give error and prompt to install
# print(heroes.gen())


# Draw a dashed line

# import turtle as t
#
# tim = t.Turtle()
# tim.color("fuchsia")
#
# for i in range(10):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()
#
# screen = t.Screen()
# screen.exitonclick()


# Draw different shapes in different colors

# import turtle as t
# import random as r
#
# tim = t.Turtle()
# t.colormode(255)  # changes colormode of Turtle MODULE.
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for j in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# def change_color():
#     r_val = r.randint(1, 255)
#     g_val = r.randint(1, 255)
#     b_val = r.randint(1, 255)
#     rgb = (r_val, g_val, b_val)
#     return rgb
#
#
# for sides_in_shape in range(3, 11):
#     tim.pencolor(change_color())
#     draw_shape(sides_in_shape)
#
#
# screen = t.Screen()
# screen.exitonclick()


# # Random walk
#
# import turtle as t
# import random as r
#
# tim = t.Turtle()
# tim.pensize(10)
# tim.speed(10)
# screen = t.Screen()
# color_palette = ["#3B9AB2", "#78B7C5", "#EBCC2A", "#E1AF00", "#F21A00"]
# directions = [0, 90, 180, 270]
#
# for step in range(100):
#     tim.pencolor(r.choice(color_palette))
#     tim.setheading(r.choice(directions))
#     # tim.right(r.choice(directions))  # could use instead of "setheading", also works
#     tim.forward(30)
#
# screen.exitonclick()


# Tuples

# my_tuple = (1, 3, 8)
# my_tuple[0]  # 1 ... similar to a list.. what's the diff?
# # cannot change values in tuple. it's immutable, cannot be changed
# list(my_tuple)  # converts to list


# Draw a Spirograph!

# import turtle as t
# import random as r
#
# tim = t.Turtle()
# t.colormode(255)
# tim.speed("fastest")
#
# color_palette = ["#85D4E3", "#F4B5BD", "#9C964A", "#CDC08C", "#FAD77B"]
# gap_size = 5
#
#
# def draw_spirograph(size_of_gap, size_of_circle):
#     for step in range(int(360 / size_of_gap)):
#         tim.pencolor(r.choice(color_palette))
#         tim.setheading(step * size_of_gap)
#         tim.circle(size_of_circle)
#
#
# draw_spirograph(30, 50)
#
# screen = t.Screen()
# screen.exitonclick()
