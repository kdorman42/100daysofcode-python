from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float)

    def __repr__(self):
        return f'<Book {self.id}: {self.title}, {self.author} - Rating: {self.rating}>'

# ------ INITIALIZE DB -------#
# db.create_all()

# ----- INSERT ROW (CREATE A RECORD) -------#
# harry_potter = Books(title="Harry Potter", author="J.K. Rowling", rating=5)
# zen = Books(title="Zen and the Art of Motorcycle Maintenance", author="Robert Pirsig", rating=9.5)
# db.session.add(harry_potter)
# db.session.add(zen)
# db.session.commit()

print(Books.query.all())