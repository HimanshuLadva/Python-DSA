-- https://leetcode.com/problems/invalid-tweets?envType=problem-list-v2&envId=database

select tweet_id from Tweets 
where len(content) > 15