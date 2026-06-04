# https://leetcode.com/problems/sum-of-unique-elements/?envType=problem-list-v2&envId=counting

from typing import List
from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
       c = Counter(nums)
       ans = 0
       for (key, value) in c.items():
            if value == 1:
                ans += key
       
       return ans
    
sol = Solution()
sol.sumOfUnique(nums = [1,2,3,2])