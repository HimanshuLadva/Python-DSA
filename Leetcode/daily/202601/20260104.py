# https://leetcode.com/problems/four-divisors?envType=daily-question&envId=2026-01-04

from typing import List
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors(n):
            print(f"step-1: {int(n ** 0.5)}")
            divisors = set()
            for i in range(1, int(n ** 0.5)+1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                    print(f"step-2: {i} {n // i}")
            return sorted(divisors)
        
        ans = 0
        for num in nums:
            divisors = get_divisors(num)
            print(divisors)
            if len(divisors) == 4:
                ans += sum(divisors)                
        return ans
    # TLE
    def sumFourDivisorsV1(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            dividors = [x for x in range(1, num+1) if num % x == 0]
            if len(dividors) == 4:
                ans += sum(dividors)            
        return ans
    
sol = Solution()
nums = [21,4,7]
sol.sumFourDivisors(nums)