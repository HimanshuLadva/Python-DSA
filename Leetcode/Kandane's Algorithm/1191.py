# https://leetcode.com/problems/k-concatenation-maximum-sum/description/
#howtowork
#revision
from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        curr_sum = 0 
        max_sum = 0
        MOD = 10**9 + 7
        total = sum(arr)

        def kandane(nums):
            curr = best = 0

            for num in nums:
                curr += num
                best = max(best, curr)

                if curr < 0:
                    curr = 0

            return best

        if k == 1:
            return kandane(arr)

        for i in range(2):
            for num in arr:
                curr_sum += num
                max_sum = max(max_sum, curr_sum) % MOD

                if curr_sum < 0:
                    curr_sum = 0

        if total > 0:
            max_sum += (k - 2) * total
        # print(max_sum)
        return max_sum % MOD

sol = Solution()
# sol.kConcatenationMaxSum(arr = [1,2], k = 3)
sol.kConcatenationMaxSum(arr = [1,-2,1], k = 5)