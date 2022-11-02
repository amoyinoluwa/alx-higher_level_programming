-- Select only non-null
SELECT score, name FROM second_table AS s
WHERE name IS NOT NULL
ORDER BY s.score;
