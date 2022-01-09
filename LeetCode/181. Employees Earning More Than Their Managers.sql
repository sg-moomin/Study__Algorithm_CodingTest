/**
* LeetCode : Employees Earning More Than Their Managers
* URL : https://leetcode.com/problems/employees-earning-more-than-their-managers/
*/

/**
* Mysql
*/
select A.Name as Employee
from Employee as A, Employee as B
where A.managerId  = B.id
and A.salary > B.salary

/**
* Oracle
*/
select A.Name as Employee
from Employee A
join Employee B
on A.managerid = B.id
and A.salary > B.salary
