from dao.director import DirectorDao

class DirectorService:
    def __init__(self, director_dao = DirectorDao):
        self.director_dao = director_dao

    def get_all_directors(self):
        return self.director_dao.get_all()

    def get_one_director(self, id):
        return self.director_dao.get_one(id)