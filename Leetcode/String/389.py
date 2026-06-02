# https://leetcode.com/problems/find-the-difference/?envType=problem-list-v2&envId=string

from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = Counter(t) - Counter(s)
        return list(diff.keys())[0]
        # return next(iter(ans))
    
sol = Solution()
print(sol.findTheDifference(s = "ae", t = "aea"))