--Weather Observation Station 5
--https://www.hackerrank.com/challenges/weather-observation-station-5/problem

SELECT city, LENGTH(city)
FROM(
    SELECT city, LENGTH(city) as min_city
    FROM station
    ORDER BY min_city ASC
    LIMIT 3) as sub_query
ORDER BY city ASC
LIMIT 1;

SELECT city, LENGTH(city) as max_city
FROM station
ORDER BY max_city DESC
LIMIT 1;
