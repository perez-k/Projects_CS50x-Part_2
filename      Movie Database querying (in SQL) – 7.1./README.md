# Movie Relational Database Querying 

### Description
A set of SQL querying tasks performed on a relational database containing information about movies, actors, and directors.  
Focuses on writing queries to retrieve, filter, and analyze data from multiple interconnected tables.

---
The database, `movies.db` is a SQLite database that stores data from [IMDb](/https://www.imdb.com/) about movies, the people who directed and starred in them, and their ratings.
There is 05 tables in the database:
- `movies` table: has an id column that uniquely identifies each movie, as well as columns for the title of a movie and the year in which the movie was released. 
- `people` table: has an id column, and columns for each person’s name and birth year.
- `ratings` table: store the movie ratings. The first column in the table is movie_id, a foreign key that references the id of the movies table. The rest of the row contains data about the rating for each movie and the number of votes the movie has received on IMDb.
- `stars` and `directors` tables: match people to the movies in which they acted or directed. (Only principal stars and directors are included.) Each table has just two columns: movie_id and person_id, which reference a specific movie and person, respectively.

The goal is to write SQL queries to answer a variety of different questions by selecting data from one or more of the tables.

- In 1.sql, a SQL query to list the titles of all movies released in 2008.
query should output a table with a single column for the title of each movie.
- In 2.sql, a SQL query to determine the birth year of Emma Stone.
query should output a table with a single column and a single row (not including the header) containing Emma Stone’s birth year.
Assume that there is only one person in the database with the name Emma Stone.
- In 3.sql, a SQL query to list the titles of all movies with a release date on or after 2018, in alphabetical order.
query should output a table with a single column for the title of each movie.
Movies released in 2018 are included, as well as movies with release dates in the future.
- In 4.sql, a SQL query to determine the number of movies with an IMDb rating of 10.0.
query should output a table with a single column and a single row (not including the header) containing the number of movies with a 10.0 rating.
- In 5.sql, a SQL query to list the titles and release years of all Harry Potter movies, in chronological order.
query should output a table with two columns, one for the title of each movie and one for the release year of each movie.
may assume that the title of all Harry Potter movies will begin with the words “Harry Potter”, and that if a movie title begins with the words “Harry Potter”, it is a Harry Potter movie.
- In 6.sql, a SQL query to determine the average rating of all movies released in 2012.
query should output a table with a single column and a single row (not including the header) containing the average rating.
- In 7.sql, a SQL query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title.
query should output a table with two columns, one for the title of each movie and one for the rating of each movie.
Movies that do not have ratings should not be included in the result.
- In 8.sql, a SQL query to list the names of all people who starred in Toy Story.
query should output a table with a single column for the name of each person.
may assume that there is only one movie in the database with the title Toy Story.
- In 9.sql, a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.
query should output a table with a single column for the name of each person.
People with the same birth year may be listed in any order.
No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order.
If a person appeared in more than one movie in 2004, they should only appear in your results once.
- In 10.sql, a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.
query should output a table with a single column for the name of each person.
If a person directed more than one movie that received a rating of at least 9.0, they should only appear in your results once.
- In 11.sql, a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
query should output a table with a single column for the title of each movie.
may assume that there is only one person in the database with the name Chadwick Boseman.
- In 12.sql, a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.
query should output a table with a single column for the title of each movie.
may assume that there is only one person in the database with the name Johnny Depp.
may assume that there is only one person in the database with the name Helena Bonham Carter.
- In 13.sql, a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
query should output a table with a single column for the name of each person.
There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
Kevin Bacon himself should not be included in the resulting list.


Note: The database was too heavy to be added to the repository. You can find it directly on [cs50 website](https://cs50.harvard.edu/college/2020/spring/psets/7/movies/)


### **Key Concepts**
- **Relational Database Queries** – retrieving and analyzing data from related tables, using table relationships via primary and foreign keys.  
- **Table Joins** – using `JOIN` clauses to combine data from multiple tables (`INNER JOIN`, `LEFT JOIN`, ...).  
- **Filtering Data** – refining results based on multiple conditions (e.g., year, rating, genre) with `WHERE`.  
- **Aggregation** – using functions like `COUNT()` and `AVG()` to summarize data.  
- **Sorting Results** – ordering outputs with `ORDER BY` for clarity.  


---

### **Example Query**
```bash
$ cat filename.sql | sqlite3 movies.db > output.txt

```

```sql
SELECT movies.title
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON people.id = stars.person_id
WHERE people.name = 'Emma Stone';
```