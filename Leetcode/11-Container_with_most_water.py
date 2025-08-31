# https://leetcode.com/problems/container-with-most-water?envType=problem-list-v2&envId=array
from typing import List

class Solution:
    # using two pointer approach
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            temp = min(height[i], height[j]) * (j-i)
            if temp > max_area:
                max_area = temp
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
    
    def maxAreaV1(self, height: List[int]) -> int:
        max_area = 0
        for i,x in enumerate(height):
            for j in range(i+1,len(height)):
                temp = min(x,height[j]) * (j-i)
                if temp > max_area:
                    max_area = temp

        return max_area
    
s = Solution()
height = [1,8,6,2,5,4,8,3,7]
# height = [2,6,9,10,5,8,7]
# height = [9,5,2,6,7,10,2]
print(s.maxArea(height))