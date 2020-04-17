--The Report
--https://www.hackerrank.com/challenges/the-report/problem

SELECT
    CASE
        WHEN grade <= 7 THEN NULL
        ELSE name
        END AS name, grade, marks
        FROM(
            SELECT name, grade, marks
            FROM(
                SELECT *
                FROM students
                CROSS JOIN grades) AS grade
            WHERE min_mark <= marks and marks <= max_mark) as sub_query
    ORDER BY grade DESC, name ASC, marks ASC;
