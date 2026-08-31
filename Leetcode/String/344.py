# https://leetcode.com/problems/reverse-string/description/

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        

sol = Solution()
sol.reverseString(s = ["h","e","l","l","o"])
        