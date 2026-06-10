# https://leetcode.com/problems/maximum-total-subarray-value-ii/?envType=daily-question&envId=2026-06-10

from typing import List
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        values = []

        for i in range(n):
            curr_min = nums[i]
            curr_max = nums[i]

            for j in range(i+1, n):
                curr_min = min(curr_min, nums[j])
                curr_max = max(curr_max, nums[j])
                
                values.append(curr_max - curr_min)

        values.sort(reverse=True)
        return sum(values[:k])
    
    # MLE
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = set()

        for i in range(n):
            for j in range(i+2, n+1):
                s.add(tuple(nums[i:j]))

        values = []
        for subarry in s:
            values.append(abs(min(subarry) - max(subarry)))
        
        values.sort(reverse=True)
        return sum(values[:k+1])
    
sol = Solution()
# print(sol.maxTotalValue(nums = [1,3,2], k = 2))
# print(sol.maxTotalValue(nums = [4,2,5,1], k = 3))
print(sol.maxTotalValue(nums = [11, 8], k = 2))