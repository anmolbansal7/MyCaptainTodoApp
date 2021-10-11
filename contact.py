from flask import Flask
from flask_sqalchemy import SQLAlchemy
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:7898994162k@localhost:5432/'

db = 