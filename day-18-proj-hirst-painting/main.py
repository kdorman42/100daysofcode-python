# Gets color palette from Hirst painting in image.jpg
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

import turtle as t
import random as r

color_list = [(240, 242, 246), (237, 231, 214), (218, 234, 224), (141, 176, 206), (25, 32, 48), (28, 105, 156), (208, 161, 112), (238, 222, 234), (230, 211, 94), (131, 31, 64), (5, 162, 195), (182, 45, 84), (217, 60, 85), (226, 80, 44), (195, 129, 168), (54, 167, 116), (29, 61, 115), (108, 181, 91), (109, 99, 88), (2, 102, 119), (193, 187, 47), (241, 204, 1), (19, 22, 21), (52, 149, 109), (171, 211, 173), (226, 170, 186), (150, 207, 222), (234, 169, 160), (184, 186, 210), (115, 38, 37)]
t.colormode(255)
print(t.screensize())

timmy = t.Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
timmy.goto(-400, 300)

n_rows = int(t.screensize()[1] / 100 * 2) + 1
n_col = int(t.screensize()[0] / 100 * 2)

for row in range(n_rows):
    for col in range(n_col):
        timmy.dot(50, r.choice(color_list))
        timmy.forward(100)
    if row % 2 == 0:
        turn_angle = 90
    else:
        turn_angle = -90
    timmy.dot(50, r.choice(color_list))
    timmy.right(turn_angle)
    timmy.forward(100)
    timmy.right(turn_angle)

screen = t.Screen()
screen.exitonclick()