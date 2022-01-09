/**
* LeetCode : Consecutive Numbers
* URL : https://leetcode.com/problems/consecutive-numbers/
*/

FROM
    Logs log1,
    Logs log2,
    Logs log3
WHERE
    log1.id = log2.id - 1
    and log2.id = log3.id -1
    and log1.num = log2.num
    and log2.num = log3.num
;
