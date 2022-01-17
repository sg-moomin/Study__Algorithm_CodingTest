/**
* LeetCode : Trips and Users
* URL :https://leetcode.com/problems/trips-and-users/
*/

/*
* AVG  사용
*/

select trip_totals.day,
,round(avg(trip_totals.status like '%cancel%'), 2) as "Cancellation Rate"
from (
    select trips.request_at as day
    ,trips.status
    from Trips trips, Users clients, Users drivers
    where trips.request_at between '2013-10-01' and '2013-10-03'
    and (clients.users_id = trips.client_id   and clients.banned = 'No')
    and (drivers.users_id = trips.driver_id and drivers.banned = 'No')
) trip_totals
group by day


/*
* join 사용
*/

select trip_totals.day,
round(avg(trip_totals.status like '%cancel%'), 2) as "Cancellation Rate"
from (
    select trips.request_at as day
    ,trips.status
    from Trips trips
    left join Users clients
    on clients.users_id = trips.client_id
    left join Users drivers
    on drivers.users_id = trips.driver_id
    where trips.request_at between '2013-10-01' and '2013-10-03'
    and clients.banned = 'No'
    and drivers.banned = 'No'
) trip_totals
group by day
