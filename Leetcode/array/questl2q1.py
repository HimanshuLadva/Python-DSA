# https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        dublicate = -1
        n = len(nums)

        for num in nums:
            if num in seen:
                dublicate = num
            seen.add(num)
        
        total = sum(nums)
        expected = (n * (n + 1)) // 2

        # print(total, expected)
        missing = expected - (total - dublicate)
        return [dublicate, missing]
    
    def findErrorNumsV1(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dublicate = 0
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                dublicate = nums[i]
                break
        
        for i in range(1, n+1):
            if nums[i-1] != i:
                return [dublicate, i]
        return []
    
sol = Solution()
sol.findErrorNums([1,2,2,4])
                