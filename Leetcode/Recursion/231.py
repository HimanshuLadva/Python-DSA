# https://leetcode.com/problems/power-of-two?envType=problem-list-v2&envId=recursion

class Solution:
    def isPowerOfTwo(self, n: int , power:int = 1) -> bool:
        if 2**power == n:
            return True
        elif 2**power > n:
            return False
        
        return self.isPowerOfTwo(n, power + 1)
    
sol = Solution()
n = 64
print(sol.isPowerOfTwo(n))