# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/?envType=daily-question&envId=2026-01-16
from typing import List
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)

        hFences.sort()
        vFences.sort()
        hlen = len(hFences)
        vlen = len(vFences)
        h_set = set()
        v_set = set()

        for i in range(hlen):
            for j in range(i+1, hlen):
                h_set.add(hFences[j] - hFences[i])

        for i in range(vlen):
            for j in range(i+1, vlen):
                v_set.add(vFences[j] - vFences[i])

        # print(v_set, h_set)
        intersaction = h_set & v_set
        # print(intersaction)
        if intersaction:
            max_e = max(intersaction)
            return (max_e * max_e) % MOD
        else:
            return -1
    
sol = Solution()
m = 4
n = 3
hFences = [2,3]
vFences = [2]
print(sol.maximizeSquareArea(m, n, hFences, vFences))