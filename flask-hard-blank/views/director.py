from flask_restx import Resource, Namespace
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class directorsView(Resource):
    def get(self):
        return director_service.get_all_directors(), 200

@director_ns.route('/<int:gid>')
class directorView(Resource):
    def get(self, gid):
        return director_service.get_one_director(gid), 200