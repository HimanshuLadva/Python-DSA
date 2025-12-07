# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range?envType=daily-question&envId=2025-12-07

import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
    
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low + 1
        if diff%2 == 1:
            if low%2 == 0:
               return math.floor(diff / 2)
            else:
               return math.ceil(diff / 2)
        
        return diff//2