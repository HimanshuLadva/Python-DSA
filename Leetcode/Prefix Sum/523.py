# https://leetcode.com/problems/continuous-subarray-sum/description/
from typing import List
class Solution:
    #implogic
    #revision
    #howtowork
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        left = 0
        prefix = 0
        remainder_index = {0: -1}

        for right in range(n):
            # print(remainder_index)
            prefix += nums[right]

            remainder = prefix % k

            #formula: If two prefix sums have the same remainder when divided by k, the elements between them have a sum divisible by k.
            if remainder in remainder_index:
                left = remainder_index[remainder]

                if right - left >= 2:
                    return True
            else:
                remainder_index[remainder] = right

        return False

sol = Solution()
sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6)