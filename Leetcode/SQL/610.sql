-- https://leetcode.com/problems/triangle-judgement?envType=problem-list-v2&envId=database
-- Triangle Judgement
select *,
case when (x+y)>z and (x+z)>y and (y+z)>x then 'Yes' else 'No' end as triangle
from Triangle