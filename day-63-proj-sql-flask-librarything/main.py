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


@app.route('/')
def home():
    all_books = Books.query.all()
    return render_template('index.html', books_list=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        book = Books(title=request.form['title_input'],
                     author=request.form['author_input'],
                     rating=request.form['rating_input'])
        db.session.add(book)
        db.session.commit()
        redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    book_id = request.args['id']
    book_to_edit = Books.query.filter_by(id=book_id).first()
    if request.method == "POST":
        book_to_edit.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', edit_book=book_to_edit)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    book_id = request.args['id']
    book_to_delete = Books.query.filter_by(id=book_id).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

