# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/?envType=daily-question&envId=2026-01-17
# #learntopic-intersection_area function
from typing import List
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        blen = len(bottomLeft)
        max_area = 0

        def intersection_area(b1,t1,b2,t2):
            x_overlap = max(0, min(t1[0], t2[0]) - max(b1[0],b2[0]))
            y_overlap = max(0, min(t1[1], t2[1]) - max(b1[1],b2[1]))
            return x_overlap, y_overlap
        
        for i in range(blen):
            for j in range(i+1, blen):
                x_overlap,y_overlap = intersection_area(
                    bottomLeft[i],topRight[i],
                    bottomLeft[j],topRight[j]
                )
                side = min(x_overlap, y_overlap)
                max_area = max(max_area, side * side)

        return max_area
    
sol = Solution()
bottomLeft = [[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]
print(sol.largestSquareArea(bottomLeft, topRight))