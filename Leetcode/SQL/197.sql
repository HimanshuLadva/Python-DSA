-- https://leetcode.com/problems/rising-temperature?envType=problem-list-v2&envId=database
-- #MIMP

select a.id from Weather a
join Weather b on a.recordDate= DATEADD(day, 1, b.recordDate)
where a.temperature > b.temperature