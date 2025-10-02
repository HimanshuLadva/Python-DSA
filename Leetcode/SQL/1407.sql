-- https://leetcode.com/problems/top-travellers?envType=problem-list-v2&envId=database

;with ctee as (
select u.id,COALESCE(sum(distance), 0) as travelled_distance from Users u
left outer join Rides r on r.user_id = u.id
group by u.id
) select Users.name,travelled_distance from ctee
left outer join Users on Users.id = ctee.id
order by travelled_distance desc,Users.name