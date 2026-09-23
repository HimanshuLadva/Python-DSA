# https://leetcode.com/problems/reverse-string/description/

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(i, j):
            if i >= j:
                return

            s[i],s[j] = s[j],s[i]
            reverse(i+1,j-1)

        reverse(0,len(s) - 1)
        
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            s[i],s[j]=s[j],s[i]

            i += 1
            j -= 1

sol = Solution()
# sol.reverseString(s = ["h","e","l","l","o"])
sol.reverseString(s = ["H","a","n","n","a","h"])