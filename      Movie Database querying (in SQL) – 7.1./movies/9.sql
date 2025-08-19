SELECT DISTINCT people.name FROM people JOIN stars JOIN movies ON people.id = stars.person_id AND stars.movie_id = movies.id 
WHERE movies.year = 2004 
ORDER BY people.birth;