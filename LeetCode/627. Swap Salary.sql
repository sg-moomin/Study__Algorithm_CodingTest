/**
* LeetCode : Swap Salary
* URL : https://leetcode.com/problems/swap-salary/
*/

update Salary
set
    sex = (case when sex = 'f' then 'm'
                when sex = 'm' then 'f'
                end);
