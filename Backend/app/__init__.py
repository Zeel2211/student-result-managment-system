from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)
CORS(app)

from app import db, routes, auth
