from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models.users import db, User  # Import the db and User model from models.users

app = Flask(__name__)
CORS(app)

# Configure SQLAlchemy to use MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://khayo:kiatu254@localhost:5000/twakula_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Define route for creating a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    # Get user details from request body
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Create a new user object
    new_user = User(username=username, email=email, password=password)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
    app.run()
