# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2026-05-23

from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        
        return count <= 1
    # 4ms
    def check(self, nums: List[int]) -> bool:
        sorted_arr = sorted(nums)
        n = len(nums)

        for i in range(n):
            nums.insert(0, nums.pop(n-1))

            if nums == sorted_arr:
                return True
            
        return False
    
sol = Solution()
sol.check(nums = [3,4,5,1,2])