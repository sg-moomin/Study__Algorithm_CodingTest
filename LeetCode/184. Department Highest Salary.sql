/**
* LeetCode : Department Highest Salary
* URL : https://leetcode.com/problems/department-highest-salary/
*/

select D.name as Department
,E.name as Employee
,E.salary as Salary
From Department D, Employee E
,(Select max(Salary) as ranks,
     DepartmentId,
     Name,
     Salary
     from Employee
    group by DepartmentId) as duals
where duals.departmentId = D.id
and E.Salary = duals.ranks
and E.departmentId = duals.DepartmentId
