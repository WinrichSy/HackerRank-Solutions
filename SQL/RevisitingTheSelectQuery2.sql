--Revisiting the Select Query 2
--https://www.hackerrank.com/challenges/revising-the-select-query-2/problem

SELECT name FROM CITY
WHERE CountryCode LIKE("USA")
    AND Population > 120000
ORDER BY Population DESC;
