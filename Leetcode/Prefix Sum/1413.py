# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/?envType=problem-list-v2&envId=prefix-sum

from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]

        # print(prefix)
        min_value = min(prefix)
        startValue = 1 - min_value
        # print(startValue)

        while True:
            temp_sum = startValue
            for num in nums:
                temp_sum += num
            
            if temp_sum > 0:
                return startValue if startValue else 1

            startValue += 1
    
sol = Solution()
print(sol.minStartValue(nums = [-3,2,-3,4,2]))
# print(sol.minStartValue(nums = [1,2]))