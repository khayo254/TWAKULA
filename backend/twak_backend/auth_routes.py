from flask import Blueprint, request, jsonify

authbp = Blueprint('auth', __name__)

users = []
is_logged_in = False

@authbp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    if any(user['username'] == username for user in users):
        return jsonify({"error": "Username already exists"}), 400
    
    user = {"username": username, "password": password}
    users.append(user)
    
    return jsonify({"message": "User registered successfully!"}), 201

@authbp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    user = next((user for user in users if user['username'] == username and user['password'] == password), None)
    
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401
    
    return jsonify({"message": "User logged in successfully"}), 200

@authbp.route('/logout', methods=['GET'])
def logout():
    global is_logged_in
    
    if not is_logged_in:
        return jsonify({"error": "User is not logged in"}), 401

    return jsonify({"message": "User logged out successfully"}), 200
