# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/?envType=daily-question&envId=2026-04-21
#newlearn
#revision
#howtowork
from typing import List
from math import inf
from collections import Counter
class Solution:
    def isAllConnected(self, source: List[int],allowedSwaps: List[List[int]]):
        n = len(source)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a,b):
            parent[find(a)] = find(b)

        for a,b in allowedSwaps:
            union(a, b)
        
        group = {}
        for i in range(n):
            group.setdefault(find(i), []).append(i)
        
        # print(f"group = {group}")
        return group

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # print(f"start = {source}")

        m = len(allowedSwaps)
        res = inf

        group = self.isAllConnected(source, allowedSwaps)
        if m > 0 and len(group) == 1 and sorted(source) == sorted(target):
            return 0

        print(group)
        res = 0
        for g in group:
            s = Counter(source[i] for i in group[g])
            t = Counter(target[i] for i in group[g])
            print(f"{s}, {t}")

            for val in t:
                matched = min(s[val], t[val])
                res += t[val] - matched
    
        return res
    
sol = Solution()
# print(sol.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3],[0,3]]))
print(sol.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]))
# print(sol.minimumHammingDistance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []))
# print(sol.minimumHammingDistance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]))
# print(sol.minimumHammingDistance(source = [86], target = [49], allowedSwaps = []))
# print(sol.minimumHammingDistance(source = [71,13,6,60,22,31], target = [66,57,2,60,22,73], allowedSwaps = [[4,5],[0,4]]))
        