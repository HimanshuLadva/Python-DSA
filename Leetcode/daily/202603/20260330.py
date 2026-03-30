from typing import List
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return (sorted(s1[::2]) == sorted(s2[::2]) and
                sorted(s1[1::2]) == sorted(s2[1::2]))
    
sol = Solution()
# sol.canBeEqual(s1 = "abcd", s2 = "cdab")
sol.canBeEqual(s1 = "bnxw", s2 = "bwxn")