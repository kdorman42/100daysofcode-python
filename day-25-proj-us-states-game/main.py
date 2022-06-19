import turtle as t
import pandas as pd

continue_game = True
score = 0
correct_states = []
image = 'blank_states_img.gif'


def write_state_name(state, x, y):
    cursive = t.Turtle()
    cursive.hideturtle()
    cursive.penup()
    cursive.color("black")
    cursive.goto(x, y)
    cursive.write(arg=state, align="left", font=("Courier", 10, "normal"))


screen = t.Screen()
screen.title("The US States Game")

screen.addshape(image)
t.shape(image)

# prints coordinates when you click on the map
# don't need because this is already included in the csv
# def get_mouse_click_coor(x, y):
#     print(x, y)
# t.onscreenclick(get_mouse_click_coor)

game_data = pd.read_csv('50_states.csv')

while continue_game:

    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state =="Exit":
        missed_states = [state for state in game_data.state.values if state not in correct_states]
        pd.DataFrame(data=missed_states, columns=['States to Learn']).to_csv('states_to_learn.csv')
        break

    if answer_state in game_data.state.values and answer_state not in correct_states:
        xcor = int(game_data[game_data.state == answer_state].x)
        ycor = int(game_data[game_data.state == answer_state].y)
        write_state_name(answer_state, xcor, ycor)
        correct_states.append(answer_state)
        score = len(correct_states)
        if score == 50:
            continue_game = False

t.mainloop()  # keeps the screen open (similar to exitonclick)


