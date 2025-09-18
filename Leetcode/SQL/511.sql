-- https://leetcode.com/problems/game-play-analysis-i?envType=problem-list-v2&envId=database

select player_id,min(event_date) as first_login from Activity
group by player_id