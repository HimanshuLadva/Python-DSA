# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=problem-list-v2&envId=sliding-window

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window = sum(nums[:k])
        
        max = window / k
        for i in range(n-k):
            window = window - nums[i] + nums[i+k]

            current = window / k
            if current > max:
                max = current
            
        return max
    
sol = Solution()
sol.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)