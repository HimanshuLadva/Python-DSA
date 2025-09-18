# Equal Row and Column Pairs
# MIMP
from collections import Counter

class Solution:
    def countOfEqualPairs(self, grid):
        n = len(grid)
        lookup = {}

        """ for row in grid:
            temp = tuple(row)
            if temp not in lookup:
                lookup[temp] = 0
            lookup[temp] += 1
         """
        lookup = Counter(tuple(row) for row in grid)
        ans = 0
        for i in range(n):
            temp = tuple(grid[j][i] for j in range(n))
            print(f"temp = {temp}")

            if temp in lookup:
                ans += lookup[temp]
            else:
                ans += 0

        print(lookup)
        return ans



    def equalPairs(self, grid):
        n = len(grid)
       
        # Step 1: Count frequency of each row
        row_count = Counter(tuple(row) for row in grid)
        
        # Step 2: Build each column and compare with rows
        ans = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))  # build column j
            ans += row_count[col]  # add matches (0 if not found)
        
        return ans
    
sol = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# print(sol.equalPairs(grid))
print(sol.countOfEqualPairs(grid))
