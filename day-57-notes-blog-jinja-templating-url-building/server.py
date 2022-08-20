from flask import Flask, render_template
import random
from datetime import datetime
import requests

AGIFY_URL = 'https://api.agify.io?name='
GENDERIZE_URL = 'https://api.genderize.io?name='

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("my_website.html",
                           num=random_number, copyright_year=current_year)


@app.route('/guess/<name_input>')
def guess(name_input):
    name_input = name_input.title()
    r_agify = requests.get(AGIFY_URL + name_input)
    agify_guess = r_agify.json()["age"]
    r_genderize = requests.get(GENDERIZE_URL + name_input)
    genderize_guess = r_genderize.json()["gender"]
    return render_template("guess.html",
                           name=name_input, age=agify_guess, gender=genderize_guess)


@app.route('/blog/<num2>')
def get_blog(num2):
    # print(num2)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    r = requests.get(blog_url)
    all_posts = r.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)