from dao.model.genre import Genre, GenreSchema

class GenreDao:
    def __init__(self, session):
        self.session = session
    
    def get_all(self):
        genres = Genre.query.all()
        genresSchema = GenreSchema(many=True)
        return genresSchema.dump(genres)

    def get_one(self, id):
        genre = Genre.query.get(id)
        genreSchema = GenreSchema()
        return genreSchema.dump(genre)