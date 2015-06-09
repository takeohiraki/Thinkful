-- Finds the mean of the average high temperature 
-- for all of the cities within a state

-- SELECT cities.state, AVG(Average_high) 
-- FROM weather 
-- JOIN cities ON weather.city = cities.name
-- GROUP BY cities.state;


------------------------------------------------------------------
-- Finds the mean of the average high temperatures for all 
-- of the cities within a state, starting with the hottest

-- SELECT cities.state, AVG(Average_high) AS avg_high_temp
-- FROM weather 
-- JOIN cities ON weather.city = cities.name
-- GROUP BY cities.state
-- ORDER BY avg_high_temp DESC;


------------------------------------------------------------------
-- Finds the mean of the average high temperatures for 
-- all of the cities within a state, starting with the 
-- hottest, and filtering out states with a mean above 65F.

-- SELECT cities.state, AVG(Average_high) AS avg_high_temp
-- FROM weather 
-- JOIN cities ON weather.city = cities.name
-- GROUP BY cities.state
-- HAVING avg_high_temp < 65
-- ORDER BY avg_high_temp DESC;


SELECT * FROM weather
LEFT OUTER JOIN cities ON weather.city = cities.name;