# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение

# Пример

from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movie_ns
from views.genre import genre_ns
from views.director import director_ns

# from models import Review, Book
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app
def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)

if __name__ == '__main__':
    config = Config()
    app = create_app(config)
    app.run(host="localhost", port=10001, debug = False)
