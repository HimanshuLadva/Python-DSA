# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/?envType=problem-list-v2&envId=sliding-window

from typing import List
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        window = s[:3]
        s_window = set(window)

        if len(window) == len(s_window):
            count += 1

        for i in range(n-3):
            window = window[1:] + s[i + 3]
            s_window = set(window)
            if len(window) == len(s_window):
                count += 1     
                
        return count

sol = Solution()
sol.countGoodSubstrings(s = "xyzzaz")