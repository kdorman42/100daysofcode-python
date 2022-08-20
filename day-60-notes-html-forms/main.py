from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def receive_data():
    error = None
    if request.method == 'POST':
        name_store = request.form['name_input']
        pw_store = request.form['pw_input']
    return render_template('boop.html', name=name_store, pw=pw_store)


if __name__ == "__main__":
    app.run(debug=True)