# https://leetcode.com/problems/angle-between-hands-of-a-clock/description/?envType=daily-question&envId=2026-06-18
 
class Solution:
    #formula clock angle = |30H - 5.5M|
    def angleClock(self, hour: int, minutes: int) -> float:
        return min(abs((30 * hour) - (5.5 * minutes)), 360 - abs((30 * hour) - (5.5 * minutes)))
    
sol = Solution()
print(sol.angleClock(hour= 12, minutes= 30))