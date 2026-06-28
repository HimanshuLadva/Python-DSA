# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/?envType=daily-question&envId=2026-06-28
from typing import List
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        arr[0] = 1

        for i in range(n-1):
            if abs(arr[i] - arr[i+1]) > 1:
                arr[i+1] = (arr[i] + 1)
        
        return max(arr)
    
sol = Solution()
print(sol.maximumElementAfterDecrementingAndRearranging(arr = [2,2,1,2,1]))
print(sol.maximumElementAfterDecrementingAndRearranging(arr = [100,1,1000]))
print(sol.maximumElementAfterDecrementingAndRearranging(arr = [1,2,3,4,5]))