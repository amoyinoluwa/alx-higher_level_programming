-- Selects records greater than 10
SELECT score, name FROM second_table as s
WHERE score >= 10
ORDER BY s.score DESC;
