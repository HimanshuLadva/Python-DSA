# https://leetcode.com/problems/minimum-time-to-make-rope-colorful?envType=daily-question&envId=2025-11-03
# #MIMP

from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        i = 0
        while i < len(colors) - 1:
            if colors[i] == colors[i+1]:
                time += min(neededTime[i], neededTime[i+1])
                neededTime[i+1] = max(neededTime[i], neededTime[i+1])
            i += 1
        return time
    
    def minCostV1(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        j = 1
        colorlen = len(colors)
        time = 0
        while j < colorlen and i < colorlen:
            if colors[i] == colors[j]:
                if neededTime[i] < neededTime[j]:
                    time += neededTime[i]
                else:
                    time += neededTime[j]
            i += 1
            j += 1
        
        return time

sol = Solution()
colors = "abaac"
neededTime = [1,2,3,4,5]
colors = "abc"
neededTime = [1,2,3]
colors = "aabaa"
neededTime = [1,2,3,4,1]
colors = "aaaaa"
neededTime = [1,2,3,4,1]
colors = "aaabbbabbbb"
neededTime = [3,5,10,7,5,3,5,5,4,8,1]
print(sol.minCost(colors, neededTime))