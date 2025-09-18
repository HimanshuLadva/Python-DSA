-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends?envType=problem-list-v2&envId=database

;with ctee as (
select accepter_id as num,count(accepter_id) as cnt from RequestAccepted
group by accepter_id
union all
select requester_id as num,count(requester_id) as cnt from RequestAccepted
group by requester_id
)
select top 1 num as id,SUM(cnt) as num from ctee
group by num
order by SUM(cnt) desc