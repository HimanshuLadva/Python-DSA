-- https://leetcode.com/problems/swap-salary?envType=problem-list-v2&envId=database

update Salary set sex = (case when sex = 'f' then 'm' else 'f' end)