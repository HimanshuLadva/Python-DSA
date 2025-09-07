# https://leetcode.com/problems/assign-cookies?envType=problem-list-v2&envId=two-pointers
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        j = 0
        g_len = len(g)
        s_len = len(s)
        g.sort()
        s.sort()

        counter = 0
        while i < g_len and j < s_len:
            if g[i] <= s[j]:
                counter += 1
                i += 1
                j += 1
            elif g[i] > s[j]:
                j += 1
            else:
                i += 1

        return counter
    
s1 = Solution()
g = [1,2,3]
# s = [1,2]
s = [3]
# g = [10,9,8,7]
# s = [5,6,7,8]
print(s1.findContentChildren(g, s))