# https://leetcode.com/problems/separate-squares-ii/?envType=daily-question&envId=2026-01-14
# #learntopic-caculate_area_below()
# #newlearn
from typing import List
from bisect import bisect_left

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Create events for y-sweepline
        y_events = []
        for x, y, l in squares:
            y_events.append((y, 1, x, l))      # Square starts at y
            y_events.append((y + l, -1, x, l))  # Square ends at y+l
        
        y_events.sort()
        
        # Process events and compute cumulative area
        cumulative_areas = [(y_events[0][0], 0)]  # (y_coord, area_below_y)
        active_squares = []  # List of (x, l) for squares that are active
        prev_y = y_events[0][0]
        
        for y, delta, x, l in y_events:
            # Compute area added from prev_y to y
            if active_squares and y > prev_y:
                width = self.get_union_width(active_squares)
                area_added = width * (y - prev_y)
                prev_area = cumulative_areas[-1][1]
                cumulative_areas.append((y, prev_area + area_added))
            elif y > prev_y:
                cumulative_areas.append((y, cumulative_areas[-1][1]))
            
            # Update active squares
            if delta == 1:
                active_squares.append((x, l))
            else:
                active_squares.remove((x, l))
            
            prev_y = y
        
        # Binary search for target area
        total_area = cumulative_areas[-1][1]
        target = total_area / 2.0
        
        # Find where area crosses target
        idx = bisect_left([a for y, a in cumulative_areas], target)
        
        if idx == 0:
            return cumulative_areas[0][0]
        if idx >= len(cumulative_areas):
            return cumulative_areas[-1][0]
        
        y1, a1 = cumulative_areas[idx - 1]
        y2, a2 = cumulative_areas[idx]
        
        if abs(a2 - a1) < 1e-12:
            return (y1 + y2) / 2.0
        
        # Linear interpolation
        ratio = (target - a1) / (a2 - a1)
        return y1 + ratio * (y2 - y1)
    
    def get_union_width(self, squares):
        """Get total width covered by squares (union of x-intervals)"""
        if not squares:
            return 0
        
        intervals = [(x, x + l) for x, l in squares]
        intervals.sort()
        
        total = 0
        start, end = intervals[0]
        
        for x1, x2 in intervals[1:]:
            if x1 <= end:
                end = max(end, x2)
            else:
                total += end - start
                start, end = x1, x2
        
        total += end - start
        return total
    
sol = Solution()
# squares = [[0,0,1],[2,2,1]]
squares = [[0,0,2],[1,1,1]]
print(sol.separateSquares(squares))