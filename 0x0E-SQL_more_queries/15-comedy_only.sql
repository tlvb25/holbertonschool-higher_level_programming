-- ONLY COMEDY
SELECT tv_genres.name
FROM tv_show
INNER JOIN tv_genres
ON tv_show.id=tv_genres.id
INNER JOIN tv_show_genres
ON tv_show_genres.show_id=tv_genres.id
WHERE tv_genres.name='Comedy'
ORDER BY tv_shows.title ASC;
