# https://leetcode.com/problems/count-number-of-trapezoids-ii?envType=daily-question&envId=2025-12-03
# #newlearn
from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    # 959ms
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10**9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        ans = 0
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2
                
                if x2 == x1:
                    k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx
                
                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)

        for sti in slope_to_intercept.values():
            if len(sti) == 1:
                continue
            
            cnt = defaultdict(int)
            for b_val in sti:
                cnt[b_val] += 1
            
            total_sum = 0
            for count in cnt.values():
                ans += total_sum * count
                total_sum += count

        for mts in mid_to_slope.values():
            if len(mts) == 1:
                continue
            
            cnt = defaultdict(int)
            for k_val in mts:
                cnt[k_val] += 1
            
            total_sum = 0
            for count in cnt.values():
                ans -= total_sum * count
                total_sum += count
        
        return ans
    # 4130ms
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """
        Count the number of trapezoids that can be formed from given points.
        
        Key Optimization Strategy:
        Instead of checking every pair of segments for collinearity (O(n^4)),
        we group segments by their LINE (not just slope) to automatically handle
        collinear segments. This reduces complexity significantly.
        
        Algorithm:
        1. Group all segments by the LINE they lie on (using line equation ax + by = c)
        2. Group all lines by their SLOPE (to find parallel lines)
        3. For each pair of parallel lines, multiply their segment counts
        4. Subtract parallelograms (counted twice due to having 2 pairs of parallel sides)
        
        Time Complexity: O(n^2 * log(r)) where n = points, r = coordinate range
        Space Complexity: O(n^2)
        
        This approach automatically handles:
        - Collinear points (grouped on same line, don't form trapezoids)
        - Disjoint segments (counted correctly)
        - Parallelograms (identified by shared midpoint, subtracted once)
        """
        n = len(points)
        
        def get_line(p1, p2):
            """
            Get line equation as normalized (a, b, c) where ax + by = c.
            This uniquely identifies a line regardless of which 2 points we choose on it.
            
            Returns: (a, b, c) in normalized form
            """
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            
            # Degenerate case: same point
            if dx == 0 and dy == 0:
                return None
            
            # Normalize direction vector
            g = gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g
            
            # Line equation: dy * x - dx * y = dy * x1 - dx * y1
            # This gives us ax + by = c where:
            a = dy
            b = -dx
            c = dy * p1[0] - dx * p1[1]
            
            # Normalize: ensure first non-zero coefficient is positive
            if a < 0 or (a == 0 and b < 0):
                a, b, c = -a, -b, -c
            
            # Further normalize by GCD of all coefficients
            g = gcd(gcd(abs(a), abs(b)), abs(c)) if c != 0 else gcd(abs(a), abs(b))
            if g > 0:
                a //= g
                b //= g
                c //= g
            
            return (a, b, c)
        
        # Step 1: Group all segments by the line they lie on
        # Key insight: All collinear segments will be in the same group
        line_segments = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                line = get_line(points[i], points[j])
                if line:
                    line_segments[line].append((i, j))
        
        # Step 2: Group lines by their slope
        # Lines with the same slope are parallel
        slope_lines = defaultdict(list)
        
        for line in line_segments.keys():
            a, b, c = line
            
            # Extract slope from line equation ax + by = c
            # slope = -a/b (if b != 0), or infinity (if b == 0)
            if b == 0:
                slope = (float('inf'), 0)  # Vertical line
            elif a == 0:
                slope = (0, 1)  # Horizontal line
            else:
                # Normalize slope as a fraction
                g = gcd(abs(a), abs(b))
                slope = (-a // g, b // g)
                # Ensure consistent sign
                if slope[1] < 0:
                    slope = (-slope[0], -slope[1])
            
            slope_lines[slope].append(line)
        
        result = 0
        
        # Step 3: Count trapezoids
        # For each pair of parallel lines (same slope, different intercept),
        # every combination of one segment from each line forms a trapezoid
        for slope, lines in slope_lines.items():
            num_lines = len(lines)
            
            # For each pair of parallel lines
            for i in range(num_lines):
                for j in range(i + 1, num_lines):
                    line1 = lines[i]
                    line2 = lines[j]
                    
                    # Number of segments on each line
                    segs1 = line_segments[line1]
                    segs2 = line_segments[line2]
                    
                    # Each combination forms a trapezoid
                    result += len(segs1) * len(segs2)
        
        # Step 4: Subtract parallelograms
        # A parallelogram has TWO pairs of parallel sides, so it gets counted twice
        # We identify parallelograms by checking if two segments share the same midpoint
        midpoint_map = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                # Use doubled coordinates to avoid floating point
                mid_x = points[i][0] + points[j][0]
                mid_y = points[i][1] + points[j][1]
                midpoint_map[(mid_x, mid_y)].append((i, j))
        
        parallelograms = 0
        
        for mid, segments in midpoint_map.items():
            if len(segments) >= 2:
                # Group these segments by their line
                # (segments on the same line don't form a parallelogram)
                seg_lines = defaultdict(list)
                for seg in segments:
                    line = get_line(points[seg[0]], points[seg[1]])
                    seg_lines[line].append(seg)
                
                # Count pairs of segments from DIFFERENT lines
                lines_list = list(seg_lines.keys())
                for i in range(len(lines_list)):
                    for j in range(i + 1, len(lines_list)):
                        # Each pair forms a parallelogram
                        parallelograms += len(seg_lines[lines_list[i]]) * len(seg_lines[lines_list[j]])
        
        # Subtract parallelograms (they were counted twice)
        result -= parallelograms
        
        return result