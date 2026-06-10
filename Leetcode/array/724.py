from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        prev_sum = 0

        for i,num in enumerate(nums):
            if prev_sum == s-num-prev_sum:
                return i
            prev_sum += num
        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if sum(nums[0:i]) == sum(nums[i+1:n]):
                return i
        return -1
    
sol = Solution()
sol.pivotIndex(nums = [1,7,3,6,5,6])