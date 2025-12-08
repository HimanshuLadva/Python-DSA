# https://leetcode.com/problems/count-square-sum-triples?envType=daily-question&envId=2025-12-08
from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c = int(sqrt(a**2 + b**2 + 1))
                if c <= n and c**2 == a**2 + b**2:
                    count += 1
        return count
    
    def countTriplesV1(self, n: int) -> int:
        arr = [x**2 for x in range(1,n+1)]
        count = 0
        print(arr)
        for i in range(1, n):
            print(i**2 + (i+1)**2)
            if i**2 + (i+1)**2 in arr:
                count += 2
        return count
    
sol = Solution()
# print(sol.countTriples(5))
print(sol.countTriples(10))