# https://leetcode.com/problems/trionic-array-i/?envType=daily-question&envId=2026-02-03
from typing import List
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        first = 0
        second = 0
        third = 0
        n = len(nums)
        print(f"arr = {nums}")
        for i in range(n-1):
            print(f"first = {nums[i]}")
            if nums[i] < nums[i+1]:
                first = i+1
            else:
                break

        for j in range(first, n-1):
            print(f"second = {nums[j]}")
            if nums[j] > nums[j+1]:
                second = j+1
            else:
                break
        
        for k in range(second, n-1):
            print(f"third = {nums[k]}")
            if nums[k] < nums[k+1]:
                third = k+1
            else:
                third = 0
                break
        
        print(f"first, second, third = {first} {second} {third}")
        return bool(first and second and third)  

sol = Solution()
nums = [1,3,5,4,2,6]
nums = [3,4,3,7,4,7]
print(sol.isTrionic(nums))  