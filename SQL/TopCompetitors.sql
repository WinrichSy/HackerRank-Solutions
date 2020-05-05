--Top Competitors
--https://www.hackerrank.com/challenges/full-score/problem

SELECT sq.hacker_id, sq.name
FROM(
    SELECT h.hacker_id, h.name, COUNT(s.score) as total_score
    FROM hackers h
    LEFT JOIN submissions s
    ON h.hacker_id = s.hacker_id
    JOIN challenges c
    ON c.challenge_id = s.challenge_id
    JOIN difficulty d
    ON d.difficulty_level = c.difficulty_level
    WHERE d.score = s.score
    GROUP BY h.hacker_id, h.name
    HAVING total_score > 1
    ORDER BY total_score DESC, h.hacker_id) AS sq;
