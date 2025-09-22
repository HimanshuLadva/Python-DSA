# https://leetcode.com/problems/sort-colors?envType=problem-list-v2&envId=two-pointers
# MIMP
from collections import Counter

class Solution(object):
    def sortColors(self, nums):
        start,mid = 0,0
        end = len(nums) - 1

        while mid <= end:
            if nums[mid] == 0:
                nums[start],nums[mid] = nums[mid],nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[end] = nums[end],nums[mid]
                end -= 1
                
        print(nums)
    
    def sortColorsV1(self, nums):
        lookup = Counter(nums)
        i = 0
        for x in range(3):
            for y in range(lookup[x]):
                nums[i] = x
                i += 1

        print(nums)
    
sol = Solution()
nums = [2,0,2,1,1,0]
nums= [1,2,0]
nums= [0,1,2,0,1,2]
# nums = [2,0,1]
# nums = [1,0,2]
sol.sortColors(nums)