# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock?envType=daily-question&envId=2025-12-15

from typing import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        count = n
        conseccutive = 0

        for i in range(n-1):
            if prices[i] - prices[i+1] == 1:
                conseccutive += 1
                count += conseccutive
            else:
                conseccutive = 0

        return count
    
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        count = 0
        for i in range(n):
            j = i
            
            while j < n-1 and prices[j] - prices[j+1] == 1:
                j += 1

            count += (j - i + 1)
        return count
    
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        count = 0
        for i in range(n):
            for j in range(i, n):
                temp = prices[i:j+1]
                tlen = len(temp)
                k = 0
                flag = True
                while k < tlen-1:
                    if temp[k] - temp[k+1] != 1:
                        flag = False
                    k += 1
                    
                if flag:
                    count += 1
        return count
    
sol = Solution()
prices = [3,2,1,4]
prices = [8,6,7,7]
# prices = [1,2,3,4,5]
print(sol.getDescentPeriods(prices))