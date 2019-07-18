-- MY GENRES
SELECT tv_genres.name AS 'name'
FROM tv_genres
INNER JOIN tv_shows, tv_show_genres
ON tv_genres.id=tv_show_genres.show_id=tv_shows.id
WHERE tv_shows.id = "Dexter"
ORDER BY tv_genres.name ASC;
