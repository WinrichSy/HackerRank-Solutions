--Revisitng the Select Query 1
--https://www.hackerrank.com/challenges/revising-the-select-query/problem

SELECT * FROM CITY
WHERE population > 100000
    AND countrycode LIKE("USA")
ORDER BY population DESC;
