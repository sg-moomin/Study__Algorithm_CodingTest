/**
* LeetCode : Delete Duplicate Emails
* URL : https://leetcode.com/problems/delete-duplicate-emails/
*/

delete per1
from Person per1
join Person per2
on per1.email = per2.email
where per1.id > per2.id


/**
* 안되는 이유를 모르겠음 
*/
select min(per1.id) as id, per1.email as email
from Person per1
group by per1.email
order by per1.id asc
