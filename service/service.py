from dao import dao

class Service:

    dao = dao.DaoFactory()

    dao = dao.create()

    def get_movie_titles_from_title(self,title):
        list = []
        for m in self.dao.get_all_movies():
            if m.title.lower().find(title) != -1:
                list.append(m.title)
        return list

    def get_movie_from_title(self,_title):
        return self.dao.get_movie_from_title(_title)


    def get_review_from_title(self,_title):
        movie_id = self.dao.get_movie_id_from_movie_title(_title)
        return self.dao.get_review_from_movie_id(movie_id)

    def commit(self):
        self.dao.commit()

    def update_movie(self, movie, title, genre, lead_studio, profit, ww_gross, year):
        self.dao.update_movie(movie, title, genre, lead_studio, profit, ww_gross, year)

    def update_review(self, review , audience_score, rt_score):
        self.dao.update_review(review, audience_score, rt_score)
