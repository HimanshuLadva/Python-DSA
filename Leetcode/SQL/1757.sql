-- https://leetcode.com/problems/recyclable-and-low-fat-products?envType=problem-list-v2&envId=database

select product_id from Products where low_fats = 'Y' and recyclable = 'Y'