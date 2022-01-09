/**
* LeetCode : Duplicate Emails
* URL : https://leetcode.com/problems/duplicate-emails/
*/


/* Solution 1 */
select duals.email as Email
from (
    SELECT id, email, count(email) as numEmail
    from Person
    group by email
) as duals
where duals.numEmail > 1

/* Solution 2 */
select email as Email
from Person
group by email
having count(email) > 1
