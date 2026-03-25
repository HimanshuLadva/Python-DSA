# https://leetcode.com/problems/equal-sum-grid-partition-i/?envType=daily-question&envId=2026-03-25
#implogic
from typing import List
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        # horizontal
        current = 0
        for row in grid:
            current += sum(row)
            if current == total - current:
                return True
        
        # vertical
        current = 0
        for col in zip(*grid):
            current += sum(col)
            if current == total - current:
                return True
            
        return False
    
sol = Solution()
sol.canPartitionGrid(grid = [[1,4],[2,3]])
sol.canPartitionGrid([[28443],[33959]])