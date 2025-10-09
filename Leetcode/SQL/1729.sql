-- https://leetcode.com/problems/find-followers-count?envType=problem-list-v2&envId=database

select user_id,count(distinct follower_id) as followers_count from Followers
group by user_id
order by user_id