-- Number of shows by genre
SELECT tv_genres.name as genre,
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id=tv_genres.genre_id
GROUP BY tv_genres.name;
