SELECT movies.title FROM movies JOIN ratings JOIN stars JOIN people ON movies.id = ratings.movie_id AND ratings.movie_id = stars.movie_id AND stars.person_id = people.id
WHERE people.name = "Chadwick Boseman" 
ORDER BY ratings.rating DESC 
LIMIT 5;