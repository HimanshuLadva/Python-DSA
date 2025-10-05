-- https://leetcode.com/problems/fix-names-in-a-table?envType=problem-list-v2&envId=database
-- #MIMP 
select user_id,UPPER(LEFT(name, 1)) + LOWER(SUBSTRING(name, 2, LEN(name))) as name from Users
order by user_id