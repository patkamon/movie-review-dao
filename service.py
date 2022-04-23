import models


def get_movie_titles_from_title(title):
    list = []
    for m in models.session.query(models.Movie):
        if m.title.lower().find(title) != -1:
            list.append(m.title)
    return list

def get_movie_from_title(_title):
    return models.session.query(models.Movie).filter_by(title=_title).first()


def get_review_from_title(_title):
    return models.session.query(models.Review).filter_by(title=_title).first()
