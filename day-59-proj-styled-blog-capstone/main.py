from flask import Flask, render_template, request
import requests
from smtplib import SMTP
import os
from dotenv import load_dotenv

load_dotenv('../env_vars/100doc_python_env_vars.env')

sender_smtp = "smtp.mail.yahoo.com"
my_email = os.environ['MY_TEST_YMAIL']
my_password = os.environ['TEST_YMAIL_APP_PW']  # ymail app password
to_email = os.environ['MY_TEST_GMAIL']




blog_url = 'https://api.npoint.io/feb01b334e6089a26d21'
r = requests.get(blog_url)
all_posts = r.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blog_posts=all_posts)


@app.route('/blog/<int:id>')
def goto_post(id):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/about')
def about():
    pass
    return render_template("about.html")


@app.route('/contact')
def contact():
    pass
    return render_template("contact.html")


@app.route('/form-entry', methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with SMTP(sender_smtp) as connection_yahoo:
            connection_yahoo.starttls()  # creates a secure connection
            connection_yahoo.login(user=my_email, password=my_password)
            connection_yahoo.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:You've got mail!\n\n"
                    f"From: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Message: {message}")
    return render_template('form_confirmation.html')


if __name__ == "__main__":
    app.run(debug=True)
