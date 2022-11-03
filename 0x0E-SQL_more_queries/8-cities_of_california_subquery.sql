-- lists all the cities of California that can be found in the database
SELECT id, name FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE states.name = 'California')
ORDER BY cities.id;
