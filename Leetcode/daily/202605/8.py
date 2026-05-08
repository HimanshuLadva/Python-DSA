from typing import List
class Solution:
    def isPrime(self, n: int):
        if n <= 1:
            return False
        
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False

            i += 1
        return True
    
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        jump = 0
        while jump <= n-1:
            if self.isPrime(nums[jump]):
                if jump < n and nums[jump+1] % nums[jump]:
                    jump += 1
                elif jump > 0 and nums[jump-1] % nums[jump]:
                    jump -= 1
                else:
                    jump += 1
            else:
                jump += 1
        
        return jump

sol = Solution()
print(sol.minJumps(nums = [1,2,4,6]))