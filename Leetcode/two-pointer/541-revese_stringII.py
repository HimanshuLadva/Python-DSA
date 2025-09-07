# https://leetcode.com/problems/reverse-string-ii?envType=problem-list-v2&envId=two-pointers
from typing import List

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 1:
            return s 
        i = 0
        jump = (2*k)
        s = list(s)

        while i < len(s):
            if i - 1 < 0:
                s[i:i+k] = s[(i+k)-1::-1]
            else: 
                s[i:i+k] = s[(i+k)-1:i-1:-1]
            i += jump
        return "".join(s)
    
sol = Solution()
s = "abcdefg"
k = 2
print(sol.reverseStr(s, k))