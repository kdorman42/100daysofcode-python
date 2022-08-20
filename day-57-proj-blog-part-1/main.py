from flask import Flask, render_template
from post import Post
import requests

blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
r = requests.get(blog_url)
all_posts = r.json()
posts_list = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in all_posts]


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_posts=posts_list)


@app.route('/blog/<int:id>')
def goto_post(id):
    requested_post = None
    for blog_post in posts_list:
        if blog_post.id == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
