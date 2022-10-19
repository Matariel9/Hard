from dao.genre import GenreDao

class GenreService:
    def __init__(self, genre_dao = GenreDao):
        self.genre_dao = genre_dao

    def get_all_genres(self):
        return self.genre_dao.get_all()

    def get_one_genre(self, id):
        return self.genre_dao.get_one(id)