-- https://leetcode.com/problems/find-customer-referee?envType=problem-list-v2&envId=database
select name from Customer where ISNULL(referee_id, 0) <> 2
