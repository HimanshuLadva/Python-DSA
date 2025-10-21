# https://leetcode.com/problems/majority-element-ii?envType=problem-list-v2&envId=array

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        result = []
        thresold = len(nums) // 3

        if count1 > thresold:
            result.append(candidate1)
        
        if count2 > thresold and candidate1 != candidate2:
            result.append(candidate2)

        return result
    

    def majorityElementV1(self, nums: List[int]) -> List[int]:
        len_n = len(nums)
        n = int(len_n/3)
        counter_n = Counter(nums)        
        return [x for x in counter_n if counter_n[x] > n]
    
sol = Solution()
nums = [1,2]
sol.majorityElement(nums)