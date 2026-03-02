# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/?envType=daily-question&envId=2026-03-02
#newlearn
from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Count trailing zeros
        zeros = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)

        swaps = 0

        # Step 2: Fix rows one by one
        for i in range(n):
            required = n - 1 - i
            
            if zeros[i] >= required:
                continue
            
            # find row to bring up
            j = i + 1
            while j < n and zeros[j] < required:
                j += 1
            
            if j == n:
                return -1
            
            # bring it up using adjacent swaps
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                swaps += 1
                j -= 1

        return swaps

sol = Solution()
grid = [[0,0,1],[1,1,0],[1,0,0]]
sol.minSwaps(grid)