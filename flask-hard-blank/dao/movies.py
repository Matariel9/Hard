# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from dao.model.movie import Movie, MovieSchema

class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        movies = Movie.query.all()
        movies_schema = MovieSchema(many = True)
        return movies_schema.dump(movies)
    
    def post_movie(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def get_one_movie(self, id):
        movie = Movie.query.get(id)
        movie_schema = MovieSchema()
        return movie_schema.dump(movie)

    def change_one_movie(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.close

    def get(self, id):
        movie = Movie.query.get(id)
        return movie

    def delete(self, id):
        movie = Movie.query.get(id)
        self.session.delete(movie)
        self.session.commit()
        self.session.close()

    def find_by_genre(self, g_id):
        movies = Movie.query.filter(Movie.genre_id == g_id)
        movies_schema = MovieSchema(many = True)
        return movies_schema.dump(movies)

    def find_by_director(self, d_id):
        movies = Movie.query.filter(Movie.director_id == d_id)
        movies_schema = MovieSchema(many = True)
        return movies_schema.dump(movies)

    def find_by_year(self, year):
        movies = Movie.query.filter(Movie.year == year)
        movies_schema = MovieSchema(many = True)
        return movies_schema.dump(movies)

    

        