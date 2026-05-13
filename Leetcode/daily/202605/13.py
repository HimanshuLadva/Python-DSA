# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/?envType=daily-question&envId=2026-05-13
from typing import List
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        temp_arr = set()

        i = 0
        j = n-1

        while i < j:
            addition = nums[i] + nums[j]
            temp_arr.add(nums[i] + nums[j])
            i += 1
            j -= 1

        print(temp_arr)
        if len(temp_arr) == 1:
            return 0
        
        res = [x for x in temp_arr if x >= limit]
        return len(res)
    
sol = Solution()
print(sol.minMoves(nums = [1,2,4,3], limit = 4))
# print(sol.minMoves(nums = [1,2,4,10], limit = 11))