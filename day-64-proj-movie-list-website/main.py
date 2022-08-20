from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import requests
import os
from dotenv import load_dotenv

load_dotenv('../env_vars/100doc_python_env_vars.env')

TMDB_API_KEY = os.environ['TMDB_API_KEY']
TMDB_API_URL_SEARCH = 'https://api.themoviedb.org/3/search/movie'
TMDB_API_URL_MOVIE = 'https://api.themoviedb.org/3/movie/'
TMDB_IMG_BASE_URL = 'https://image.tmdb.org/t/p'


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////movie-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(1024))
    img_url = db.Column(db.String(240), nullable=False)

    def __repr__(self):
        return f'<Movie: {self.title} ({self.year})>'


class EditForm(FlaskForm):
    rating = FloatField(label="Rating (number between 0 and 10, e.g. 7.5, 2, 9.3)",
                        validators=[DataRequired(), NumberRange(min=0, max=10,
                                                                message="Rating must be between 0 and 10")])
    review = StringField(label="Review", validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddForm(FlaskForm):
    movie_search = StringField(label="Movie Title")
    search = SubmitField('Next')


@app.route("/")
@app.route("/home")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies_list=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args['id']
    movie_to_edit = Movie.query.filter_by(id=movie_id).first()
    if form.validate_on_submit():
        movie_to_edit.rating = form.rating.data
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', edit_movie=movie_to_edit, form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args['id']
    movie_to_delete = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        return redirect(url_for('select', q=form.movie_search.data))
    return render_template('add.html', form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    query = request.args['q']
    params = {
        "api_key": TMDB_API_KEY,
        "query": query
    }
    r = requests.get(TMDB_API_URL_SEARCH, params=params)
    search_results = r.json()["results"]
    return render_template('select.html', results=search_results)


@app.route("/submit_add", methods=["GET", "POST"])
def submit_add():
    tid = request.args['tid']
    params = {
        "api_key": TMDB_API_KEY
    }
    r = requests.get(f'{TMDB_API_URL_MOVIE}/{tid}', params=params)
    title_details = r.json()
    img = f'{TMDB_IMG_BASE_URL}/w500/{title_details["poster_path"]}'
    new_movie = Movie(id=tid,
                      title=title_details["title"],
                      year=title_details["release_date"][:4],
                      description=title_details["overview"],
                      img_url=img)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=tid))


if __name__ == '__main__':
    app.run(debug=True)
