-- Rotten Tomatoes
SELECT tv_shows.title, SUM(tv_show_ratings.rate) rating
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_shows.id=tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY  rating DESC;
