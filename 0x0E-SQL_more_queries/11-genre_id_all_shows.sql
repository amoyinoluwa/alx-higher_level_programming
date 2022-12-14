-- script that lists all shows contained in the database
SELECT tv.title, tvs.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tvs
ON tvs.show_id = tv.id
ORDER BY tv.title, tvs.genre_id;
