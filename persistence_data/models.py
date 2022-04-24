from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, String, Float,ForeignKey
from sqlalchemy.orm import sessionmaker

import csv

engine = create_engine('sqlite:///movie-review.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    lead_studio = Column(String)
    profit = Column(Float)
    ww_gross = Column(String)
    year = Column(Integer)

    def __repr__(self):
       return f'id = {self.id} title = {self.title} genre = {self.genre} lead studio = {self.lead_studio} profit = {self.profit} world wide gross = {self.ww_gross} year = {self.year} '

class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    movie_key = Column(Integer, ForeignKey('movie.id'))
    audience_score = Column(Integer)
    rt_score = Column(Integer)

    def __repr__(self):
       return f'id = {self.id} movie_key = {self.movie_key} audience score = {self.audience_score} Rotten Tomatoes score = {self.rt_score}'


def main():
    Base.metadata.create_all(engine)
