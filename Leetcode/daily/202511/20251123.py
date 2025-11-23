# https://leetcode.com/problems/greatest-sum-divisible-by-three?envType=daily-question&envId=2025-11-23
# #newlearn
from typing import List
class Solution:
    # 13ms
    def maxSumDivThree(self, nums: List[int]) -> int:
        sm = sum(nums)
        r = sm % 3
        if r == 0:
            return sm
        
        nm1 = [x for x in nums if x % 3 == 1]
        nm2 = [x for x in nums if x % 3 == 2]

        nm1.sort()
        nm2.sort()

        if r == 1:
            result = sm
            if len(nm1) > 0:
                result = min(result, nm1[0])
            if len(nm2) > 1:
                result = min(result, nm2[0] + nm2[1])
            return sm - result
        else:
            result = sm
            if len(nm2) > 0:
                result = min(result, nm2[0])
            if len(nm1) > 1:
                result = min(result, nm1[0] + nm1[1])
            return sm - result
        
    # 55ms
    def maxSumDivThreeV1(self, nums: List[int]) -> int:
        sum0 = 0
        sum1 = 0
        sum2 = 0

        for num in nums:
            reminder = num % 3
            temp0 = sum0
            temp1 = sum1
            temp2 = sum2

            if reminder == 0:
                sum0 = max(temp0, temp0 + num)
                if temp1 > 0: sum1 = max(temp1, temp1 + num)
                if temp2 > 0: sum2 = max(temp2, temp2 + num)
            elif reminder == 1:
                if temp2 > 0: sum0 = max(temp0, temp2 + num)
                sum1 = max(temp1, temp0 + num)
                if temp1 > 0: sum2 = max(temp2, temp1 + num)
            elif reminder == 2:
                if temp1 > 0: sum0 = max(temp0, temp1 + num)
                if temp2 > 0: sum1 = max(temp1, temp2 + num)
                sum2 = max(temp2, temp0 + num)
        return sum0

sol = Solution()
nums = [3,6,5,1,8]
print(sol.maxSumDivThree(nums))