--Type of Triangle
--https://www.hackerrank.com/challenges/what-type-of-triangle/problem

SELECT
    CASE
        WHEN A+B <= C or B+C <= A or C+A <= B THEN 'Not A Triangle'
        WHEN A = B and B = C THEN 'Equilateral'
        WHEN A = B or A = C or B = C THEN 'Isosceles'
        WHEN A != B and B != C and (A+B>C and B+C>A and C+A>B) THEN 'Scalene'
    END AS answers
    FROM triangles;
