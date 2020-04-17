--Higher Than 75 Marks
--https://www.hackerrank.com/challenges/more-than-75-marks/problem
--In Oracle

SELECT name
FROM students
WHERE marks>75
ORDER BY SUBSTR(name, -3, 3), id;
