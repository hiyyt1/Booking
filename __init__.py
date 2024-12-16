from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Инициализация приложения и базы данных
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Импортируем другие части приложения
from app import routes, models, utils
