# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor?envType=daily-question&envId=2025-12-14
# #newlearn
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        # Find all seat positions
        seats = [i for i, ch in enumerate(corridor) if ch == 'S']
        
        # Edge cases
        if len(seats) == 0 or len(seats) % 2 == 1:
            return 0
        
        # If exactly 2 seats, only 1 way
        if len(seats) == 2:
            return 1
        
        result = 1
        
        # For each pair of sections, count the gap between them
        # We look at positions between seat pairs
        for i in range(1, len(seats) - 1, 2):
            # Distance between 2nd seat of current section and 1st seat of next section
            gap = seats[i + 1] - seats[i]
            result = (result * gap) % MOD
        
        return result