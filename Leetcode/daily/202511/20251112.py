# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1?envType=daily-question&envId=2025-11-12
# #newlearn
from typing import List
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
       n = len(nums)

       if 1 in nums:
           return n - nums.count(1)
       
       overall_gcd = nums[0]
       for num in nums:
           overall_gcd = math.gcd(overall_gcd, num)
        
       if overall_gcd > 1:
           return -1
       
       min_step = float('inf')
       for start in range(n):
           curr_gcd = nums[start]
           for end in range(start,n):
               curr_gcd = math.gcd(curr_gcd, nums[end])
               if curr_gcd == 1:
                   min_step = min(min_step, end -start)
       return min_step + (n - 1)
    
    def minOperationsV1(self, nums: List[int]) -> int:
       count = 0
       numslen = len(nums)

       pairs = [(y+1,y) for y in nums if y+1 in nums]
       if len(pairs):
           nums[0] = 1
           count += 1
       else:
            for i in range(1, numslen):
                gcd = 1
                if nums[0] == (nums[i] + 1):
                    gcd = 1
                else:
                    gcd = math.gcd(nums[0], nums[i])
                nums[0] = gcd
                count += 1
                if nums[0] == 1:
                    break
       
       ans = 0
       if nums[0] != 1:
           ans = -1
       else:
           ans = (count + sum(x != 1 for x in nums))  
       return ans
    
sol = Solution()
# nums = [2,6,3,4]
nums = [4,2,6,3]
# nums = [2,10,6,14]
# nums = [6,10,15]
print(sol.minOperations(nums))