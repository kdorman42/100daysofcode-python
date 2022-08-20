from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////movie-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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

# --- Initialize --- #
# db.create_all()


# --- Add Row --- #
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


new_movie = Movie(
    title="Sing 2",
    year=2021,
    description="Buster and his new cast now have their sights set on debuting "
                "a new show at the Crystal Tower Theater in glamorous Redshore "
                "City. But with no connections, he and his singers must sneak "
                "into the Crystal Entertainment offices, run by the ruthless "
                "wolf mogul Jimmy Crystal, where the gang pitches the ridiculous "
                "idea of casting the lion rock legend Clay Calloway in their show. "
                "Buster must embark on a quest to find the now-isolated Clay and "
                "persuade him to return to the stage.",
    rating=5.0,
    ranking=20,
    review="I haven't seen this movie really.",
    img_url="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/aWeKITRFbbwY8txG5uCj4rMCfSP.jpg"
)
db.session.add(new_movie)
db.session.commit()