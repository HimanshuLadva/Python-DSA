# https://leetcode.com/problems/maximum-ice-cream-bars/description/?envType=daily-question&envId=2026-06-21

from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        count = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1

        return count
    
sol = Solution()
print(sol.maxIceCream(costs = [1,6,3,1,2,5], coins = 20))