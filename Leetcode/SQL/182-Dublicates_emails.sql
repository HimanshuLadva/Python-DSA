-- https://leetcode.com/problems/duplicate-emails?envType=problem-list-v2&envId=database
select email from (select email,COUNT(email) as countx from Person
group by email) t where t.countx > 1 

-- other way
select email from Person
group by email
having count(*) > 1