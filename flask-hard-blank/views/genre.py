from flask_restx import Resource, Namespace
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genre_service.get_all_genres(), 200

@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        return genre_service.get_one_genre(gid), 200