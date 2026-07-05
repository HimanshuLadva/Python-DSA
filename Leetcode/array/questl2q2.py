# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_sorted = sorted(nums)

        smaller = {}
        for i, num in enumerate(num_sorted):
            if num not in smaller:
                smaller[num] = i
        # print(smaller)
        return [smaller[num] for num in nums]
    
    def smallerNumbersThanCurrentV1(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(len([x for x in nums if x < num]))
        return res
    
sol = Solution()
sol.smallerNumbersThanCurrent(nums = [8,1,2,2,3])