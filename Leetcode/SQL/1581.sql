-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions?envType=problem-list-v2&envId=database

select customer_id,count(*) as count_no_trans from Visits
left outer join Transactions on Transactions.visit_id = Visits.visit_id and isnull(amount, 0) != 0
where isnull(amount, 0) = 0
group by customer_id
