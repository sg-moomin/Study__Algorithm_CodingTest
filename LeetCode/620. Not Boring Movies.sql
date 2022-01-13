/**
* LeetCode : Rising Temperature
* URL : https://leetcode.com/problems/rising-temperature/
*/

select *
from Cinema
where description <> 'boring'
and MOD(id, 2) = 1
order by rating desc
