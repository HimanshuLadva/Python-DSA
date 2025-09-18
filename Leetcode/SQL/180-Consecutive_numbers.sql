-- https://leetcode.com/problems/consecutive-numbers?envType=problem-list-v2&envId=database
;with ctee as (
select a.id,a.num from Logs a
inner join Logs b on a.id + 1 = b.id
where a.num = b.num 
)
select a.num as ConsecutiveNums from ctee a
inner join ctee b on a.id + 1  = b.id
group by a.num