from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker


import csv

engine = create_engine('sqlite:///movies-review.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Movie(Base):
    __tablename__ = 'movies'
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
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    audience_score = Column(Integer)
    rt_score = Column(Integer)

    def __repr__(self):
       return f'id = {self.id} title = {self.title} audience score = {self.audience_score} Rotten Tomatoes score = {self.rt_score}'




if __name__ == '__main__':
    Base.metadata.create_all(engine)
    
    # our_movie = session.query(Movie).filter_by(title='Zack and Miri Make a Porno').first()
    # our_review = session.query(Review).filter_by(title='Zack and Miri Make a Porno').first()
    #
    # session.commit()
