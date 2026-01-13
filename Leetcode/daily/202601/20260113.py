# https://leetcode.com/problems/separate-squares-i/description/?envType=daily-question&envId=2026-01-13
# #topic-caculate_area_below()
from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for x,y,l in squares)
        target = total_area / 2.0

        min_y = min(y for x,y,l in squares)
        max_y = max(y+l for x,y,l in squares)

        low,high = min_y,max_y
        epsilon = 1e-6

        while high - low > epsilon:
            mid = (low + high) / 2.0
            area_below = self.caculate_area_below(squares, mid)

            if area_below < target:
                low = mid
            else:
                high = mid
            
        return (low + high) / 2.0
    
    def caculate_area_below(self,squares, k):
        total = 0
        for x, y, l in squares:
            if k <= y:
                area = 0
            elif k >= y + l:
                area = l * l
            else:
                height_below = k - y
                area = l * height_below

            total += area
        return total
    
sol = Solution()
# squares = [[0,0,1],[2,2,1]]
squares = [[0,0,2],[1,1,1]]
print(sol.separateSquares(squares))