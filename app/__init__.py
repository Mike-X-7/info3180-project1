from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['UPLOAD_FOLDER'] = '/app/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mike:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)




from app import views, models
