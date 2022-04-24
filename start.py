from persistence_data import models

models.main()

file = open('movies.csv')
csvreader = models.csv.reader(file)

header = next(csvreader)
for row in csvreader:
 movie = models.Movie(title=row[0],genre=row[1],lead_studio=row[2],profit=float(row[4]),ww_gross=row[6],year=int(row[7]))
 models.session.add(movie)
 models.session.commit()
 review = models.Review(movie_key=int(movie.id), audience_score=int(row[3]),rt_score=int(row[5]))
 models.session.add(review)
 models.session.commit()
