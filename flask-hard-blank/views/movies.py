# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from lib2to3.refactor import MultiprocessingUnsupported
from flask_restx import Resource, Namespace
from implemented import movie_service
from flask import request

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_movies()
        year = request.args.get('year')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if year:
            res =  movie_service.year_search(year)
        elif director_id:
            res = movie_service.director_search(director_id)
        elif genre_id:
            res = movie_service.genre_search(genre_id)
        else:
            res = movie_service.get_movies()
        return res, 200

    def post(self):
        data = request.get_json()
        movie_service.add_movie(data)
        return "", 201

    def delete(self):
        del_id = request.get_json()
        movie_service.delete(del_id)
        return "", 201

@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one_movie(mid)
        return movie, 200

    def put(self, mid):
        data = request.get_json()
        movie_service.change_movie(data, mid)
        return "", 200

    def patch(self, mid):
        data = request.get_json()
        movie_service.change_movie_partially(data, mid)
        return "", 200
