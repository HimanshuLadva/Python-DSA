# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i?envType=daily-question&envId=2025-11-04

from typing import List
from collections import Counter
class Solution:
    # 19ms
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        i = 0
        while i < (len(nums) - k + 1):
            sub_arr = nums[i:k+i]
            count = Counter(sub_arr)
            sorted_items = sorted(count.items(), key=lambda x: (x[1], x[0]), reverse=True)
           
            if len(sorted_items) >= x:
                temp = 0
                tempsum = 0
                while temp < x:
                    tempsum += (sorted_items[temp][0] * sorted_items[temp][1])
                    temp += 1
                result.append(tempsum)
            else:
                result.append(sum(sub_arr))

            i += 1

        return result
    
sol = Solution()
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
sol.findXSum(nums, k, x)