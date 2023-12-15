from dataclasses import dataclass
from flask import Flask, abort, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
from sqlalchemy import UniqueConstraint

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/admin'
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title: str = db.Column(db.String(200))
    image: str = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer)
    product_id: int = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    print(type(Product.query.all()))
    print(Product.query.all())

    for product in Product.query.all():
        jsonify
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def post_like(id):

    # Make request to receive random user
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')

    # Return User in json response
    json = req.json()

    try:
        # Create product User with User from endpoint
        product_user = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(product_user)
        db.session.commit()

        publish('product_liked', id)

    except:
        abort(400, 'You already liked this product')


    return jsonify({
        'message': 'success'
    })

    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')