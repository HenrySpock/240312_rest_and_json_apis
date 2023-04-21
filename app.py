"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

connect_db(app) 

with app.app_context():
    db.create_all()

# Route to get data about all cupcakes
@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=serialized_cupcakes)

# Route to get data about a single cupcake
@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()
    return jsonify(cupcake=serialized_cupcake)

# Route to create a cupcake
@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    flavor = request.json.get('flavor')
    size = request.json.get('size')
    rating = request.json.get('rating')
    image = request.json.get('image', 'https://tinyurl.com/demo-cupcake')

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = new_cupcake.serialize()
    return jsonify(cupcake=serialized_cupcake), 201

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    flavor = request.json.get('flavor')
    size = request.json.get('size')
    rating = request.json.get('rating')
    image = request.json.get('image')

    cupcake.flavor = flavor or cupcake.flavor
    cupcake.size = size or cupcake.size
    cupcake.rating = rating or cupcake.rating
    cupcake.image = image or cupcake.image

    db.session.commit()

    serialized_cupcake = cupcake.serialize()
    return jsonify(cupcake=serialized_cupcake)

# Route to delete a cupcake
@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")

@app.route('/')
def home_page():
    return render_template('home.html')

# _________________________

if __name__ == '__main__':
    app.run(debug=True)