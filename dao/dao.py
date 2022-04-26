from persistence_data import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DaoFactory:

    def __init__(self):
        engine = create_engine('sqlite:///movie-review.db', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def create(self):
        return Dao(self.session)

class Dao:

    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(models.Movie).all()

    def get_movie_from_title(self,_title):
        return self.session.query(models.Movie).filter_by(title=_title).first()

    def get_movies_from_title(self,title):
        return self.session.query(models.Movie).filter_by(title=_title)

    def get_movie_id_from_movie_title(self,_title):
        return self.session.query(models.Movie).filter_by(title=_title).first().id

    def get_all_reviews(self):
        return self.session.query(models.Review).all()

    def get_review_from_movie_id(self,id):
        return self.session.query(models.Review).filter_by(movie_key=id).first()

    def commit(self):
        self.session.commit()

    def update_review(self, review, audience_score, rt_score):
        review.audience_score = audience_score
        review.rt_score = rt_score

    def update_movie(self, movie, title, genre, lead_studio, profit, ww_gross, year):
        movie.title = title
        movie.genre = genre
        movie.lead_studio = lead_studio
        movie.profit = profit
        movie.ww_gross = ww_gross
        movie.year = year
