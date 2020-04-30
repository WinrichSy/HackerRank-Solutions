--Top Earners
--https://www.hackerrank.com/challenges/earnings-of-employees/problem

SELECT (salary*months), COUNT(employee_id)
FROM employee
GROUP BY 1
ORDER BY 1 DESC
LIMIT 1;
