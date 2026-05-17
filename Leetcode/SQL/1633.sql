-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=problem-list-v2&envId=database

declare @user_count int = (select count(*) from Users)

select contest_id,
cast(cast(count(distinct user_id) as numeric(18,2)) / cast(@user_count as numeric(18,2)) * 100 as numeric(18,2)) as percentage
from Register
group by contest_id
order by cast(cast(count(distinct user_id) as numeric(18,2)) / cast(@user_count as numeric(18,2)) * 100 as numeric(18,2)) desc, contest_id
