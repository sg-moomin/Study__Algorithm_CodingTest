/**
* LeetCode : Second Highest Salary(두번째로 높은 급여)
* URL : https://leetcode.com/problems/second-highest-salary/
*/

SELECT max(salary) as SecondHighestSalary
FROM Employee
where salary not in (select max(salary)
                     from Employee)
