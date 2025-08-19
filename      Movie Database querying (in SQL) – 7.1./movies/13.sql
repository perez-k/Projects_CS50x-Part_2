SELECT people.name FROM people JOIN stars JOIN movies ON people.id = stars.person_id AND stars.movie_id = movies.id
WHERE movies.title IN
(SELECT movies.title FROM movies JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE people.name = "Kevin Bacon" AND people.birth = 1958);