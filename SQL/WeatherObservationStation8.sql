--Weather Observation Station 8
--https://www.hackerrank.com/challenges/weather-observation-station-8/problem

SELECT DISTINCT(city)
FROM(
    SELECT DISTINCT(city)
    FROM station
    WHERE city like '%a'
        or city like '%e'
        or city like '%i'
        or city like '%o'
        or city like '%u') as sub_query
    WHERE city like 'a%'
        or city like 'e%'
        or city like 'i%'
        or city like 'o%'
        or city like 'u%';
