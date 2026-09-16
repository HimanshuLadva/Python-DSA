# https://leetcode.com/problems/contiguous-array/

#howtowork
#revision
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0:-1}
        balance = 0
        n = len(nums)
        max_len = 0

        for i in range(n):
            if nums[i] == 0:
                balance -= 1
            else:
                balance += 1

            if balance in first:
                max_len = max(max_len, i - first[balance])
            else:
                first[balance] = i

        return max_len
    