# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/?envType=daily-question&envId=2026-03-13
#newlearn
from typing import List
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def canFinish(T):
            total = 0
            
            for w in workerTimes:
                left, right = 0, mountainHeight
                
                while left <= right:
                    mid = (left + right) // 2
                    time_needed = w * mid * (mid + 1) // 2
                    
                    if time_needed <= T:
                        left = mid + 1
                    else:
                        right = mid - 1
                
                total += right
                
                if total >= mountainHeight:
                    return True
            
            return False
        
        left, right = 0, 10**18
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if canFinish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans

sol = Solution()
mountainHeight = 10
workerTimes = [3,2,2,4]
sol.minNumberOfSeconds(mountainHeight, workerTimes)        