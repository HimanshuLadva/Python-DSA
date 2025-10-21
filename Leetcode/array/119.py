# https://leetcode.com/problems/pascals-triangle-ii?envType=problem-list-v2&envId=array
from typing import List

class Solution:
    def fact(self,num):
        f = 1
        for i in range(1, num+1):
            f *= i
        return f
    
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for j in range(0, rowIndex+1):
            result.append(int(self.fact(rowIndex) / (self.fact(j) * self.fact(rowIndex - j))))
            
        return result
    
s = Solution()
print(s.getRow(3))