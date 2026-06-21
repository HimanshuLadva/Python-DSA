# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=daily-question&envId=2026-06-19

from typing import List
from math import inf
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = 0
        max_alttitude = 0
        for g in gain:
            temp += g
            max_alttitude = max(temp, max_alttitude)

        # print(temp_arr, max_alttitude)
        return max_alttitude

sol = Solution()
sol.largestAltitude(gain = [-5,1,5,0,-7])
sol.largestAltitude(gain = [-4,-3,-2,-1,4,3,2])