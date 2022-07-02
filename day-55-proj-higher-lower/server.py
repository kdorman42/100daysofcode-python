from flask import Flask
import random

app = Flask(__name__)
COLORS = ["blue", "green", "red", "orange", "purple", "turquoise", "pink"]
GUESS_GIF = 'https://media.giphy.com/media/Zs91qfVhDfh6k2ohJ9/giphy.gif'
CORRECT_GIF = 'https://media.giphy.com/media/kyLYXonQYYfwYDIeZl/giphy.gif'
WRONG_GIF = 'https://media.giphy.com/media/AS5YEjTdZZo6WYsoZP/giphy.gif'
WUT_GIF = 'https://media.giphy.com/media/oBJ3iITOA7mBG/giphy.gif'
number = random.randint(0, 9)


def guess_decorator(fun):
    def wrapper(*args, **kwargs):
        hint, gif = fun(*args, **kwargs)
        color = random.choice(COLORS)
        text = f"<h1 style='color: {color}'>{hint}</h1>" \
               f"<p><img src={gif} width=400</p>"
        return text
    wrapper.__name__ = fun.__name__
    return wrapper


@app.route('/')
def guess_a_number():
    return f"<h1>Guess a number between 0 and 9</h1><br><br>" \
           f"<img src={GUESS_GIF} width=400>"


@app.route('/<int:guess>')
@guess_decorator
def check_answer(guess):
    if guess == number:
        hint = f"You got it! It was {number}."
        gif = CORRECT_GIF
    elif guess < 0 or guess > 9:
        hint = f"What happened? You didn't enter a number between 0 and 9."
        gif = WUT_GIF
    elif guess < number:
        hint = f"Sorry, too low..."
        gif = WRONG_GIF
    elif guess > number:
        hint = f"Sorry, too high..."
        gif = WRONG_GIF
    else:
        hint = f"What happened? You didn't enter a number between 0 and 9."
        gif = WUT_GIF
    return hint, gif


if __name__ == "__main__":
    app.run(debug=True)

