-- https://leetcode.com/problems/article-views-i?envType=problem-list-v2&envId=database

select author_id as id from Views
where viewer_id = author_id
group by author_id