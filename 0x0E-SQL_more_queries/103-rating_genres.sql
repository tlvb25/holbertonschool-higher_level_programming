-- Best genre
SELECT tv_genres.name, SUM(tv_show_ratings.rate) rating
FROM tv_show_genres
LEFT JOIN tv_show_ratings
ON tv_show_genres.show_id=tv_show_ratings.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
