--Ollivander's Inventory
--https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

SELECT subquery2.I, subquery2.A, subquery2.WNN, subquery2.P
FROM
    (SELECT MIN(W1.COINS_NEEDED) AS WN, WP1.AGE as AG, W1.POWER AS PW
     FROM WANDS W1
     INNER JOIN WANDS_PROPERTY WP1
     ON W1.CODE=WP1.CODE
     GROUP BY W1.POWER, WP1.AGE ORDER BY W1.POWER DESC, WP1.AGE DESC) subquery1
INNER JOIN
(SELECT W.ID AS I, MIN(W.COINS_NEEDED) AS WNN, WP.AGE as A, W.POWER AS P
 FROM WANDS W
 INNER JOIN WANDS_PROPERTY WP
 ON W.CODE=WP.CODE
 WHERE WP.IS_EVIL=0
 GROUP BY W.POWER, WP.AGE, W.ID
 ORDER BY W.POWER DESC, WP.AGE DESC) subquery2
ON subquery1.WN=subquery2.WNN AND subquery1.PW=subquery2.P AND subquery1.AG=subquery2.A;
