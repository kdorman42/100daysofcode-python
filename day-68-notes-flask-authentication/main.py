from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

# Generate an actual secret key using something like:
# $ python -c 'import secrets; print(secrets.token_hex())'
app.config['SECRET_KEY'] = 'not-so-secret-key-because-github'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/static/files'
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        user_exists = User.query.filter_by(email=request.form['email']).first()
        if not user_exists:
            pass_hash = generate_password_hash(password=request.form['password'],
                                               method='pbkdf2:sha256',
                                               salt_length=8)
            new_user = User(
                email=request.form['email'],
                password=pass_hash,
                name=request.form['name']
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Logged in successfully.')
            return redirect(url_for('secrets'))
        else:
            error = 'User email already exists'
    return render_template("register.html", error=error)


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None:
            error = 'User email not found'
        elif not check_password_hash(user.password, request.form['password']):
            error = 'Invalid password'
        else:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('secrets'))
    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    name = session.get('name', None)
    return render_template("secrets.html", name=name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
