--Weather Observation Station 11
--https://www.hackerrank.com/challenges/weather-observation-station-11/problem

SELECT DISTINCT(city)
FROM station
WHERE (city not like 'a%'
    and city not like 'e%'
    and city not like 'i%'
    and city not like 'o%'
    and city not like 'u%')
    or
    (city not like '%a'
    and city not like '%e'
    and city not like '%i'
    and city not like '%o'
    and city not like '%u');
