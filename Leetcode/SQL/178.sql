-- https://leetcode.com/problems/rank-scores/?envType=problem-list-v2&envId=database

select score, DENSE_RANK() over (order by score desc) as rank 
from Scores 
order by score desc