# #------- USING SQLITE --------#

# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# cursor.execute(
#     "CREATE TABLE books ("
#     "id INTEGER PRIMARY KEY,"
#     "title varchar(250) NOT NULL UNIQUE,"
#     "author varchar(250) NOT NULL UNIQUE,"
#     "rating FLOAT NOT NULL"
#     ")"
# )
#
# cursor.execute(
#     "INSERT INTO books VALUES("
#     "1, 'Harry Potter', 'J.K. Rowling', '9.3')"
# )
# db.commit()

# #------- USING SQLALCHEMY --------#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
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
# book = Books(title="Another Book", author="Another Author", rating=6)
# db.session.add(book)
# db.session.commit()

# ---- DELETE ------ #
# book_ids = [1,2,3]
# for id in book_ids:
#     book_to_delete = Books.query.get(id)
#     db.session.delete(book_to_delete)
# db.session.commit()

print(Books.query.all())
