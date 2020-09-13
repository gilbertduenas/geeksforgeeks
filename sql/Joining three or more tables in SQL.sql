/* https://www.geeksforgeeks.org/joining-three-tables-sql/ */

SELECT T1.id,
       T1.name,
       T1.cell
FROM table1 T1
JOIN table2 T2 ON T1.id = T2.id
JOIN table3 T3 ON T2.sub_group = T3.sub_group
WHERE T1.earnings > T3.earnings
GROUP BY T1.id,
         T1.name,
         T1.cell
HAVING COUNT(T2.id) > 1
ORDER BY COUNT(T2.id) DESC, T2.id;
