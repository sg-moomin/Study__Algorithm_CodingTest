/**
* LeetCode : Customers Who Never Order
* URL : https://leetcode.com/problems/customers-who-never-order/
*/

SELECT cust.name as Customers
FROM Customers as cust
LEFT JOIN Orders as ord
on cust.id = ord.CustomerId
where ord.CustomerId is null;
