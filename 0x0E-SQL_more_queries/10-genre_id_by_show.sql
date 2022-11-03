-- Genre by show
SELECT tv.title, tvs.genre_id
FROM tv_shows AS tv
JOIN tv_show_genres AS tvs
ON tvs.show_id = tv.id
ORDER BY tv.title, tvs.genre_id;
