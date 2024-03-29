from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth_routes import authbp
from profile_routes import profilebp
from recipe_routes import recipebp

app = Flask(__name__, static_folder='frontend/build/static')
CORS(app)

# Configure SQLAlchemy to use MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://khayo:kiatu254@localhost:5000/twakula_users'  # Change the URI according to your MySQL setup
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
DB = SQLAlchemy(app)

# Register blueprints for auth, profile, and recipe routes
app.register_blueprint(authbp)
app.register_blueprint(profilebp)
app.register_blueprint(recipebp)

# Routes to serve the React app
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
