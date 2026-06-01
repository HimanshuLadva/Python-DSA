from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        # print(cost)

        total = 0
        count = 0
        for c in cost:
            total += c
            count += 1
            if count == 3:
                total -= c
                count = 0
        return total
    
sol = Solution()
print(sol.minimumCost(cost = [1,2,3]))
print(sol.minimumCost(cost = [6,5,7,9,2,2]))
print(sol.minimumCost(cost = [5,5]))