/**
* LeetCode : Exchange Seats
* URL :https://leetcode.com/problems/exchange-seats/
*/

SELECT ID,
IFNULL(CASE WHEN MOD(ID, 2) != 0 THEN LEAD(student) over()
                          ELSE LAG(student) over()
                          END , student) as student
                          FROM SEAT;
