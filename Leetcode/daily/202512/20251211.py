# https://leetcode.com/problems/count-covered-buildings?envType=daily-question&envId=2025-12-11
# #newlearn
from typing import List
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        
        # Group buildings by x-coordinate (rows) and y-coordinate (columns)
        rows = {}  # x -> list of y values
        cols = {}  # y -> list of x values
        
        for x, y in buildings:
            if x not in rows:
                rows[x] = []
            if y not in cols:
                cols[y] = []
            rows[x].append(y)
            cols[y].append(x)
        
        # Sort each list
        for x in rows:
            rows[x].sort()
        for y in cols:
            cols[y].sort()
        
        # Check each building
        for x, y in buildings:
            row_list = rows[x]
            col_list = cols[y]
            
            # Building is covered if it's NOT at the extremes
            # Left: there's a building with smaller y in same row
            # Right: there's a building with larger y in same row
            # Above: there's a building with smaller x in same column
            # Below: there's a building with larger x in same column
            
            if (row_list[0] < y < row_list[-1] and 
                col_list[0] < x < col_list[-1]):
                count += 1
        
        return count
    
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        buildingset = set(map(tuple, buildings))

        for x,y in buildings:
            print(f"x = {x}, y = {y}")
            if x == 0 or y == 0 or x == n-1 or y == n-1:
                continue

            has_left = any((x-i,y) in buildingset for i in range(1, x+1))
            has_right = any((x+i,y) in buildingset for i in range(1, n-x))
            has_top = any((x,y+i) in buildingset for i in range(1, n-y))
            has_bottom = any((x,y-i) in buildingset for i in range(1, y+1))

            if has_left and has_right and has_top and has_bottom:
                count += 1

        return count
    
    def countCoveredBuildingsV1(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        xlen = len(buildings[0])
        ylen = len(buildings)

        for x,y in buildings:
            print(f"x = {x}, y = {y}")
            if x == 0 or y == 0 or x == n-1 or y == n-1:
                continue

            # left direction
            dir = x-1
            is_dir = False
            while dir >= 0:
                if [dir, y] in buildings:
                    is_dir = True
                    break
                dir -= 1
            
            # top direction
            dir = y+1
            is_dir = False
            while dir < ylen:
                if [x, dir] in buildings:
                    is_dir = True
                    break
                dir += 1

            # right direction
            dir = x+1
            is_dir = False
            while dir < xlen:
                if [dir, y] in buildings:
                    is_dir = True
                    break
                dir += 1

            # bottom direction
            dir = y-1
            is_dir = False
            while dir >= 0:
                if [x, dir] in buildings:
                    is_dir = True
                    break
                dir -= 1

            if is_dir:
                count += 1

        return count
    
sol = Solution()
n = 3
buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
print(sol.countCoveredBuildings(n, buildings))