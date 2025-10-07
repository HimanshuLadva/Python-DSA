# https://leetcode.com/problems/pascals-triangle?envType=problem-list-v2&envId=array
# #MIMP
from typing import List

class Solution:
    # 0ms
    def generate(self, numRows: int) -> List[List[int]]:
        result:List[List[int]] = []

        for i in range(0, numRows):
            temp = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1] + result[i-1][j])
            
            result.append(temp)
        return result
    
    def fact(self,num):
        f = 1
        for i in range(1, num+1):
            f *= i
        return f
    
    # 5ms
    def generateV1(self, numRows: int) -> List[List[int]]:
        result: List[List[int]] = []
        for i in range(0, numRows):
            temp = []
            for j in range(0, i+1):
                temp.append(int(self.fact(i) / (self.fact(j) * self.fact(i-j))))
            result.append(temp)

        return result
    
s = Solution()
print(s.generate(10))