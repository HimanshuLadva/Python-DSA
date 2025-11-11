# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero?envType=daily-question&envId=2025-11-10

from typing import List
class Solution:
    # 197ms
    def minOperations(self, nums: List[int]) -> int:
        stack = [-1]
        count = 0
        for x in nums:
            while stack and stack[-1] > x:
                stack.pop()

            if x > stack[-1] and x > 0:
                count += 1

            stack.append(x)
        return count
    # time limit exceeded
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while any(x != 0 for x in nums):
            elements = []
            indexs = []
            for i,x in enumerate(nums):
                if x == 0:
                    if elements:
                        min_element = min(elements)
                        temp = False
                        for j in range(len(elements)):
                            if elements[j] == min_element:
                                nums[indexs[j]] = 0
                                temp = True

                        if temp:
                            count += 1
                        
                    elements = []
                    indexs = []
                else:
                    elements.append(x)
                    indexs.append(i)

            if elements:
                min_element = min(elements)
                temp = False
                for j in range(len(elements)):
                    if elements[j] == min_element:
                        nums[indexs[j]] = 0
                        temp = True
                if temp:
                    count += 1
        return count
    
sol = Solution()
nums = [3,1,2,1]
print(sol.minOperations(nums))