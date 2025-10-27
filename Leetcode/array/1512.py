# https://leetcode.com/problems/number-of-good-pairs?envType=problem-list-v2&envId=counting

from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        lookup = {}
        for i,x in enumerate(nums):
            if x not in lookup:
                lookup[x] = []
            lookup[x].append(i)
        
        count = 0
        result = 0
        for value in lookup.values():
            for x in range(len(value)-1):
                if value[x] < value[x+1]:
                    count += 1
            if count > 0:
                result += sum(range(count+1))
            count = 0
        return result
    
sol = Solution()
nums = [1,2,3,1,1,3]
print(sol.numIdenticalPairs(nums))