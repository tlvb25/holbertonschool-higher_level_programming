-- Genre ID for all shows
SELECT title, genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id=tv_show_genres.id
ORDER BY tv_shows.title ASC
