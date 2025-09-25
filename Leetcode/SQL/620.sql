-- https://leetcode.com/problems/not-boring-movies?envType=problem-list-v2&envId=database

select * from Cinema
where description != 'boring' and id % 2 != 0
order by rating desc