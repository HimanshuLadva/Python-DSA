# https://leetcode.com/problems/last-day-where-you-can-still-cross?envType=daily-question&envId=2025-12-31
# #newlearn
from typing import List
class Solution:
    # 1499ms
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def canCross(day):
            """Check if we can cross using land cells after 'day' days"""
            # Build matrix with water up to 'day'
            matrix = [[0] * col for _ in range(row)]
            for i in range(day):
                x, y = cells[i]
                matrix[x-1][y-1] = 1  # Mark as water
            
            # BFS - only store coordinates, not full paths
            from collections import deque
            queue = deque()
            visited = set()
            
            # Add all land cells from top row to queue
            for c in range(col):
                if matrix[0][c] == 0:
                    queue.append((0, c))
                    visited.add((0, c))
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while queue:
                r, c = queue.popleft()
                
                # Check if we reached bottom row
                if r == row - 1:
                    return True
                
                # Explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (0 <= nr < row and 
                        0 <= nc < col and 
                        matrix[nr][nc] == 0 and 
                        (nr, nc) not in visited):
                        
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return False
        
        # Binary search on the answer
        left, right = 1, len(cells)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if canCross(mid):
                result = mid  # Can cross on day 'mid', try later
                left = mid + 1
            else:
                right = mid - 1  # Can't cross, try earlier
        
        return result
    
sol = Solution()
row = col = 3
cells = [[1,3],[1,2],[3,1],[3,2],[3,3],[2,3],[2,2],[2,1],[1,1]]
print(sol.latestDayToCross(row, col, cells))