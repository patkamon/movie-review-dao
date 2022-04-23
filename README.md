# movie-review-dao
 Application for checking rating of movies or other details of movies (profit, world wide gross, etc.)

Movie Table     
| Id | Title | Genre | Lead Studio | Profit | World-wide gross | Year |
|----|-------|-------|-------------|--------|------------------|------|

Review Table   
| Id | Movie id | Audience score (%) | Rotten Tomatoes score (%) |
|----|----------|--------------------|---------------------------|


# Getting Started
First run `pip3 install requirement.txt`<br/>
run `python3 start.py` to create `movie-review.db` file for tables and load data from movies.csv to db <br/>
Optional you can run `sqlite3 movie-review.db` to check current data in database <br/>
Optional run `.tables` will show you all table in `.db`<br/>
Optional run `SELECT * FROM movie` to see data in movies table <br/>
(exit from sqlite by `.exit`)<br/>
run `python3 ui.py` to use GUI of database<br/>
You can search and update them easily with `ui.py`<br/>
