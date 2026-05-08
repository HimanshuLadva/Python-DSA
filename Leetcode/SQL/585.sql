-- https://leetcode.com/problems/investments-in-2016/description/?envType=problem-list-v2&envId=database

-- first approch
;with cte as (
SELECT *,
           COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv2015_count,
           COUNT(*) OVER (PARTITION BY lat, lon) AS location_count
    FROM Insurance
) select ROUND(SUM(tiv_2016),2) as tiv_2016  from cte where location_count = 1 and tiv2015_count > 1

-- second approch
select ROUND(sum(t.tiv_2016),2) as tiv_2016 from (
select *,
count(*) over (partition by lat, lon) as location_count,
count(*) over (partition by tiv_2015) as tiv_2015_count
from Insurance
) as t where t.location_count = 1 and t.tiv_2015_count > 1