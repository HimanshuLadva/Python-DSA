# https://leetcode.com/problems/smallest-number-with-all-set-bits?envType=daily-question&envId=2025-10-29

class Solution:
    def smallestNumber(self, n: int) -> int:
        k = 1
        while True:
            temp = (2 ** k) - 1
            if temp >= n:
                return temp
            k += 1
        
        return 0
    
sol = Solution()
n = 5
print(sol.smallestNumber(n))