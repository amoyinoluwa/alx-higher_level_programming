-- Select onlu null values
SELECT tv.title, tvs.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS tvs
ON tvs.show_id = tv.id
WHERE tvs.genre_id IS NULL
ORDER BY tv.title, tvs.genre_id;
