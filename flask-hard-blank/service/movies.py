# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример
from dao.movies import MovieDao
import json

class MovieService:

    def __init__(self, movies_dao: MovieDao):
        self.movies_dao = movies_dao

    def get_movies(self):
        return self.movies_dao.get_all_movies()

    def get_one_movie(self, id):
        return self.movies_dao.get_one_movie(id)
    
    def add_movie(self, data):
        return self.movies_dao.post_movie(data)

    def genre_search(self, g_id):
        return self.movies_dao.find_by_genre(g_id)

    def director_search(self, d_id):
        return self.movies_dao.find_by_director(d_id)

    def year_search(self, y_id):
        return self.movies_dao.find_by_year(y_id)

    def change_movie_partially(self, data, id):
        movie = self.movies_dao.get(id)

        if "id" in data:
            movie.id = data["id"]
        if "title" in data:
            movie.title = data["title"]
        if "description" in data:
            movie.description = data["description"]
        if "trailer" in data:
            movie.trailer = data["trailer"]
        if "year" in data:
            movie.year = data["year"]
        if "rating" in data:
            movie.rating = data["rating"]
        if "genre_id" in data:
            movie.genre_id = data["genre_id"]
        if "director_id" in data:
            movie.director_id = data["director_id"]
        
        return self.movies_dao.change_one_movie(movie)

    def change_movie(self, data, id):
        movie = self.movies_dao.get(id)

        movie.id = data["id"]
        movie.title = data["title"]
        movie.description= data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]

        return self.movies_dao.change_one_movie(movie)     

    def delete(self, id):
        self.movies_dao.delete(id)   
