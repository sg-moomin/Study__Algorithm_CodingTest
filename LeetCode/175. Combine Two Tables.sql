/**
* LeetCode : Combine Two Tables(테이블 2개 합치기)
* URL : https://leetcode.com/problems/second-highest-salary/
*/

/*
* MySql
**/
SELECT firstName, lastName, city, state
from Person A
LEFT OUTER JOIN Address B
on A.PersonId = B.PersonId

/*
* Oracle
* (+) :  outer join
**/
SELECT firstName, lastName, city, state
from Person A ,Address B
where A.PersonId = B.PersonId(+)
