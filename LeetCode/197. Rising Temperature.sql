/**
* LeetCode : Rising Temperature
* URL : https://leetcode.com/problems/rising-temperature/
*/


# DATEDIFF를 통해 날짜의 차이를 구하는 방식
select w1.id
from Weather w1, Weather w2
where DATEDIFF(w1.recordDate, w2.recordDate) = 1
and w1.temperature > w2.temperature;

# DATE_ADD를 통해 1일 추가하는 방식
select w1.id
from Weather w1
join Weather w2
on w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
where w1.temperature > w2.temperature;
