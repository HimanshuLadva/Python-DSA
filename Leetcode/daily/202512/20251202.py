# https://leetcode.com/problems/count-number-of-trapezoids-i?envType=daily-question&envId=2025-12-02
# #newlearn
from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        levels = {}
        for x,y in points:
            levels[y] = levels.get(y, 0) + 1
        
        s1 = 0
        s2 = 0
        for n in levels.values():
            if n < 2:
                continue

            temp = n*(n-1) // 2
            s1 += temp
            s2 += temp * temp
        
        return ((s1**2 - s2) // 2) % MOD
    
    def countTrapezoidsV1(self, points: List[List[int]]) -> int:
        from collections import defaultdict

        levels = defaultdict(list)
        for x,y in points:
            levels[y].append(x)
        
        print(levels)
        segement = []
        for y in levels:
            n = len(levels[y])
            if n >= 2:
                segement.append(n*(n-1)//2)
        
        if len(segement) < 2:
            return 0
        
        s1 = sum(segement)
        s2 = sum(x**2 for x in segement)
        return (s1**2 - s2) // 2
    
    def countTrapezoidsV1(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        lookup = {}
                
        for point in points:
            if point[1] not in lookup:
                lookup[point[1]] = 0
            lookup[point[1]] += 1

        temp = []
        for x in lookup:
            if lookup[x] >= 2:
                temp.append((lookup[x] * (lookup[x] - 1))//2)

        sum_all = sum(temp)
        sum_squares = sum(x**2 for x in temp)
        result = (sum_all**2 - sum_squares) // 2

        return result
    
sol = Solution()
# points = [[0,2], [1,2], [2,2], [3,4], [4,4], [5,4], [6,4], [2,6], [3,6], [1,8], [2,8]]
points = [[0,2], [3,4],[1,2], [2,2], [4,4], [5,4], [6,4], [2,6], [3,6], [1,8], [2,8]]
print(sol.countTrapezoids(points))