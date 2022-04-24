from persistence_data import models

models.main()

file_movie = open('./data/movie-review - movie.csv')
csv_movie = models.csv.reader(file_movie)

file_review = open('./data/movie-review - review.csv')
csv_review = models.csv.reader(file_review)

header = next(csv_movie)
header = next(csv_review)

for row in csv_movie:
 movie = models.Movie(title=row[0],genre=row[1],lead_studio=row[2],profit=float(row[3]),ww_gross=row[4],year=int(row[5]))
 models.session.add(movie)
 models.session.commit()
 rev = next(csv_review)
 if row[0] == rev[0]:
     review = models.Review(movie_key=int(movie.id), audience_score=int(rev[1]),rt_score=int(rev[2]))
     models.session.add(review)
     models.session.commit()
