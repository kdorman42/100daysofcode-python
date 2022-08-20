from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint


API_KEY = "TopSecretAPIKey"

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

@app.route("/random")
def random():
    num_cafes = Cafe.query.count()
    random_cafe = Cafe.query.filter_by(id=randint(1, num_cafes)).first()
    cafe_dict = Cafe.to_dict(random_cafe)
    return jsonify(cafe_dict), 200


@app.route("/all")
def all():
    all_cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes]), 200


@app.route("/search")
def search():
    q_loc = request.args.get('loc')
    q_results = Cafe.query.filter_by(location=q_loc).all()
    if len(q_results) > 0:
        return jsonify(cafes=[cafe.to_dict() for cafe in q_results])
    else:
        return jsonify(error={"Not Found": "Sorry, no cafes found at that location."}), 404


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        has_sockets=bool(request.form.get('has_sockets')),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        seats=request.form.get('seats'),
        coffee_price=request.form.get('coffee_price')
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 200


## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    num_cafes = Cafe.query.count()
    if 1 <= cafe_id <= num_cafes:
        cafe_to_edit = Cafe.query.filter_by(id=cafe_id).first()
        cafe_to_edit.price = request.args.get('new_price')
        db.session.commit()
        return jsonify(response={"success": f"Successfully updated the price for cafe {cafe_id}"}), 200
    else:
        return jsonify(error={"Not Found": f"Cafe ID {cafe_id} not found."}), 404


## HTTP DELETE - Delete Record

@ app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
def delete_cafe(cafe_id):
    num_cafes = Cafe.query.count()
    if 1 <= cafe_id <= num_cafes:
        if request.args.get('api-key') == API_KEY:
            cafe_to_delete = Cafe.query.filter_by(id=cafe_id).first()
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted cafe {cafe_id}."}), 200
        else:
            return jsonify(error={"Not Authorized": "You need a valid API key to complete this request."}), 403
    else:
        return jsonify(error={"Not Found": f"Cafe ID {cafe_id} not found."}), 404





if __name__ == '__main__':
    app.run(debug=True)
