# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/?envType=daily-question&envId=2026-05-20

from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = []
        seen = set()
        count = 0
        for i in range(n):
            if A[i] in seen:
                count += 1
            else:
                seen.add(A[i])
            
            if B[i] in seen:
                count += 1
            else:
                seen.add(B[i])
            
            res.append(count)
        
        return res
    
    # 47ms
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = []
        for i in range(n):
            res.append(len(list(set(A[:i+1]) & set(B[:i+1]))))
            
        return res

sol = Solution()
print(sol.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))