# https://leetcode.com/problems/next-greater-element-i?envType=problem-list-v2&envId=array
# Next Greater Element I
from typing import List

class Solution:
    def nextGreaterElementV1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num1 in nums1:
            max = -999
            index = nums2.index(num1)
            
            while index < len(nums2)-1:
                if nums2[index+1] > num1:
                    max = nums2[index+1]
                    ans.append(max)
                    break   
                index += 1

            if max == -999:
                ans.append(-1)
        return ans

    def nextGreaterElementV1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for num1 in nums1:
            j = -1
            flag = False
            for index,num2 in enumerate(nums2):
                if num1 == num2:
                    j = index
                
                if j != -1 and num2 > num1:
                    ans.append(num2)
                    flag = True
                    break
            
            if j == -1 or not flag:
                ans.append(-1)
                        
        return ans
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_grater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                next_grater[stack.pop()] = num
            stack.append(num)

        for x in stack:
            next_grater[x] = -1

        return [next_grater[x] for x in nums1]
    
s = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
# nums1 = [2,4]
# nums2 = [1,2,3,4]
print(s.nextGreaterElement(nums1, nums2))