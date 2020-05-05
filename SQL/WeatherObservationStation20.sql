--Weather Observation Station 20
--https://www.hackerrank.com/challenges/weather-observation-station-20/problem

SELECT *
FROM(
    SELECT
    ROUND(LAT_N, 4) as LAT_N
    FROM station
    ORDER BY LAT_N DESC
    LIMIT 250) as sq
ORDER BY LAT_N
LIMIT 1;
