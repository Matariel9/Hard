# файл для создания DAO и сервисов чтобы импортировать их везде
from setup_db import db
from service.movies import MovieService
from service.genre import GenreService
from service.director import DirectorService
from dao.genre import GenreDao
from dao.movies import MovieDao
from dao.director import DirectorDao

movie_dao = MovieDao(db.session)
genre_dao = GenreDao(db.session)
director_dao = DirectorDao(db.session)
movie_service = MovieService(movie_dao)
genre_service = GenreService(genre_dao)
director_service = DirectorService(director_dao)
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)