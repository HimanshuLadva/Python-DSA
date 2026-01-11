# https://leetcode.com/problems/maximal-rectangle/description/?envType=daily-question&envId=2026-01-11
# #newlearn
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Update heights
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            
            # Calculate max area for current histogram
            max_area = max(max_area, self.largestRectangle(heights))
        
        return max_area
    
    def largestRectangle(self, heights):
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        # Process remaining bars
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        return max_area

