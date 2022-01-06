/**
* LeetCode : Nth Highest Salary(N번째로 높은 급여)
* URL : https://leetcode.com/problems/nth-highest-salary/
*/

CREATE FUNCTION getNthHighestSalary(N INT)
  RETURNS INT
BEGIN
  RETURN (
    SELECT distinct salary
    FROM (SELECT id, salary,
          dense_rank() over(order by salary desc) as totals
          from Employee
         ) duals
    where duals.totals = N 
  );
END
