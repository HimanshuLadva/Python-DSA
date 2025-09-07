# https://leetcode.com/problems/reverse-string?envType=problem-list-v2&envId=two-pointers

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1

        while i < j:
            s[i],s[j]=s[j],s[i]
            i += 1
            j -= 1

        return None

str = ["h","e","l","l","o"]
s = Solution()
s.reverseString(str)