--Asian Population
--https://www.hackerrank.com/challenges/asian-population/problem

SELECT SUM(city.population)
FROM city
LEFT JOIN country
ON city.countrycode = country.code
WHERE country.continent = 'Asia';
