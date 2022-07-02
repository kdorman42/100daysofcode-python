from flask import Flask

# import random

app = Flask(__name__)

# print(__name__)
# print(random.__name__)


def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function

def make_italic(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function

def make_underline(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
@make_italic
@make_underline
def goodbye():
    return 'Bye!'

# # Putting anything in the url bar in browser instead of <name> creates a variable
# with that value
# @app.route('/username/<name>')
# def greet(name):
#     return f"Hello there {name}!"

# # converter allows you to convert variable to different type - so in this case "name" is a path
# @app.route('/username/<path:name>/12')
# def greet(name):
#     return f"Hello there {name}!"

# @app.route('/username/<name>/<int:number>')
# def greet(name, number):
#     return f"Hello there {name}, you are {number}!"

@app.route('/username/<name>')
def greet(name):
    return f"<h1 style='text-align: center'>Hello there {name}!</h1>" \
           f"<p>This is a paragraph.</p>" \
           f"<img src='https://media.giphy.com/media/LZaA5gGjbUJOw/giphy.gif' width=300>"

# Runs the app
if __name__ == "__main__":
    app.run(debug=True)

