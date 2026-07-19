# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List
from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        ans = inf
        left = 0
        curr = 0

        for right in range(n):
            curr += nums[right]

            while curr >= target:
                ans = min(right - left + 1, ans)
                curr -= nums[left]
                left += 1

        return ans if ans != inf else 0
    
    #TLE
    def minSubArrayLenV2(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [nums[0]]

        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        ans = inf
        for i in range(n):
            for j in range(i, n):
                if i != 0:
                    if prefix_sum[j] - prefix_sum[i-1] >= target:
                        ans = min(j - i + 1, ans)
                else:
                    if prefix_sum[j] >= target:
                        ans = min(j - i + 1, ans)

        return ans if ans != inf else 0
    
    #TLE
    def minSubArrayLenV1(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # prefix_sum = [nums[0]]

        # for i in range(1, n):
        #     prefix_sum.append(prefix_sum[-1] + nums[i])

        pair = []
        for i in range(n):
            for j in range(i+1, n+1):
                # print(nums[i:j])
                temp = nums[i:j]
                if sum(temp) >= target:
                    pair.append(temp)

        # print(pair)
        pair.sort(key=lambda x: len(x))
        # print(pair)

        return len(pair[0]) if pair else 0
    
sol = Solution()
# print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(sol.minSubArrayLen(target = 4, nums = [1,4,4]))
# print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))
# print(sol.minSubArrayLen(target = 15, nums = [1,2,3,4,5])) #5