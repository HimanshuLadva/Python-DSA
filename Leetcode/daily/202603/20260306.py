# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/?envType=daily-question&envId=2026-03-06

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return not ('0' in s.strip('0')) 
    
    def checkOnesSegment(self, s: str) -> bool:
        result = s.strip('0')
        if '0' in result:
            return False
        
        return True

sol = Solution()
# print(sol.checkOnesSegment("110"))
# print(sol.checkOnesSegment("1001"))
# print(sol.checkOnesSegment("10"))
print(sol.checkOnesSegment("1100111"))