-- https://leetcode.com/problems/delete-duplicate-emails?envType=problem-list-v2&envId=database
--#MIMP
-- v1
delete p from Person p, Person q where q.id > p.id and p.email = q.email

-- v2
DELETE p
FROM Person p
JOIN Person q
  ON p.email = q.email
 AND p.id > q.id;