-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times?envType=problem-list-v2&envId=database

select actor_id, director_id from ActorDirector
group by actor_id, director_id 
having count(actor_id) >= 3 and count(director_id) >= 3
