# https://leetcode.com/problems/maximum-running-time-of-n-computers?envType=daily-question&envId=2025-12-01
from typing import List
class Solution:
    # 39ms
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        blen = len(batteries)
        if blen == n:
            return min(batteries)
        elif blen < n:
            return 0
        
        batteries.sort()
        s = sum(batteries)
        t = s // n
        for i in range(1, n):
            s -= batteries[-i]
            t = min(t, s // (n-i))

        return t
    
    # 1885ms
    def maxRunTimeV1(self, n: int, batteries: List[int]) -> int:
        left,right = 0, sum(batteries)

        batteries.sort()
        while left < right:
            mid = (left + right + 1) // 2
            total = 0
            for b in batteries:
                total += min(b, mid)
            
            
            if total >= n * mid:
                left = mid
            else:
                right = mid - 1

        return left

sol = Solution()
n = 2
batteries = [3,3,3]    
print(sol.maxRunTime(n, batteries))