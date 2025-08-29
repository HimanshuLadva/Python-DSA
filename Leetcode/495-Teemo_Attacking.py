# https://leetcode.com/problems/teemo-attacking?envType=problem-list-v2&envId=array
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_poison_time = 0
        n = len(timeSeries)
        for i in range(0, n-1):
            total_poison_time += min(timeSeries[i+1] - timeSeries[i], duration)
        
        total_poison_time += duration
        return total_poison_time
    
    def findPoisonedDurationV1(self, timeSeries: List[int], duration: int) -> int:
        my_arr = []
        for time in timeSeries:
            if time and my_arr and my_arr[-1] >= time:
                my_arr.pop()
                my_arr.append((time + duration - 1))
            elif time < (time + duration - 1):
                my_arr.append(time)
                my_arr.append((time + duration - 1))
            
        print(my_arr)
        return my_arr[-1]
    
s = Solution()
# timeSeries = [1,4]
timeSeries = [1,2]
timeSeries = [1,2,3,4,5,6,7,8,9]
# duration = 2
# duration = 1
duration = 100
print(s.findPoisonedDuration(timeSeries, duration))