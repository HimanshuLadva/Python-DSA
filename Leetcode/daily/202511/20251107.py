# https://leetcode.com/problems/maximize-the-minimum-powered-city?envType=daily-question&envId=2025-11-07
# #newlearn
from typing import List
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        
        # Step 1: Calculate initial power for each city
        power = [0] * n
        window_sum = 0
        
        # Initialize window for first city [0, r]
        for i in range(min(n, r + 1)):
            window_sum += stations[i]
        power[0] = window_sum
        
        # Slide window for remaining cities
        for i in range(1, n):
            if i + r < n:
                window_sum += stations[i + r]
            if i - r - 1 >= 0:
                window_sum -= stations[i - r - 1]
            power[i] = window_sum
        
        # Step 2: Binary search
        left = min(power)
        right = sum(stations) + k
        
        while left < right:
            mid = (left + right + 1) // 2
            
            if self.canAchieve(power, r, k, mid, n):
                left = mid
            else:
                right = mid - 1
        
        return left
    
    def canAchieve(self, power: List[int], r: int, k: int, target: int, n: int) -> bool:
        """
        Check if we can achieve 'target' as minimum power with k stations
        """
        # Make a copy of stations to track additions
        added = [0] * n
        stations_used = 0
        
        # Track cumulative additions using difference array
        diff = [0] * (n + 1)  # Extra space for difference array
        current_add = 0
        
        for i in range(n):
            # Update cumulative additions from difference array
            current_add += diff[i]
            
            # Current power at city i
            current_power = power[i] + current_add
            
            # Check if city i needs more power
            if current_power < target:
                needed = target - current_power
                
                # Check if we exceed k stations
                if stations_used + needed > k:
                    return False
                
                # Place stations at rightmost position that helps city i
                rightmost_pos = min(n - 1, i + r)
                
                # Update difference array
                # Stations at rightmost_pos help cities [rightmost_pos - r, rightmost_pos + r]
                left_reach = max(0, rightmost_pos - r)
                right_reach = min(n - 1, rightmost_pos + r)
                
                # Mark start of effect
                diff[left_reach] += needed
                # Mark end of effect (one position after right_reach)
                diff[right_reach + 1] -= needed
                
                stations_used += needed
                
                # Update current_add if the added stations affect current city
                if rightmost_pos >= i - r and rightmost_pos <= i + r:
                    current_add += needed
        
        return True