# https://leetcode.com/problems/max-consecutive-ones?envType=problem-list-v2&envId=array
# Max Consecutive Ones
from typing import List

class Solution:
    def findMaxConsecutiveOnesV1(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0

        if count > max_count:
            max_count = count

        return max_count
    
        def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            count = 0
            max_count = 0
            for num in nums:
                if num == 1:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    count = 0

            return max_count
    
s = Solution()
# nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]
print(s.findMaxConsecutiveOnes(nums))
        