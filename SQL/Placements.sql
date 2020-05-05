--Placements
--https://www.hackerrank.com/challenges/placements/problem

SELECT name1
FROM((
    SELECT s.name as name1, p.salary as salary1, f.friend_id
    FROM students s
    JOIN friends f
    ON s.id = f.id
    JOIN packages p
    ON p.id = s.id) as sq1
    JOIN
    (SELECT s.name as name2, p.salary as salary2, s.id
    FROM students s
    JOIN packages p
    ON p.id = s.id) as sq2
    ON sq1.friend_id = sq2.id)
WHERE salary1<salary2
ORDER BY salary2 ASC
