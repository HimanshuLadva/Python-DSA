# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/?envType=daily-question&envId=2026-04-10
from typing import List
from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        prev_indexes = defaultdict(list)
        result = 10**10

        for pos, num in enumerate(nums):
            if len(prev_indexes[num]) >= 2:
                result = min(result, pos - prev_indexes[num][-2])
            
            prev_indexes[num].append(pos)
        
        if result == 10**10:
            return -1
        return result * 2
    # 0ms
    def minimumDistance(self, nums: List[int]) -> int:
        lookup = defaultdict(list)

        for i in range(len(nums)):
            lookup[nums[i]].append(i)  

        temp = [arr for arr in lookup.values() if len(arr) >= 3]
        
        # print(temp)
        # print(lookup)
        if len(temp) == 0:
            return -1
        
        result = float('inf')
        for item in temp:
            n = len(item)
            for i in range(n):
                if i + 2 < n:
                    result = min(result, 2 * abs(item[i+2]-item[i]))   

        # print(result)
        return result
    
sol = Solution()
# sol.minimumDistance(nums = [1,1,2,3,2,1,2])
# sol.minimumDistance(nums = [1,1,1,1])
sol.minimumDistance(nums = [5,3,5,5,5])