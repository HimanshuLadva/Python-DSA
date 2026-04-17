# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/?envType=daily-question&envId=2026-04-17
from typing import List
from math import inf
#revision
#implogic
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev = dict()
        ans = inf
        for i, num in enumerate(nums):
            if num in prev:
                ans = min(ans, i - prev[num])

            prev[int(str(nums[i])[::-1])] = i

        return -1 if ans == inf else ans
    # TLE
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        
        res = 10 ** 10
        for i in range(n):
            target = int(str(nums[i])[::-1])

            is_found = False
            idx = 0
            for j in range(i+1, n):
                if nums[j] == target:
                    idx = j
                    is_found = True
                    break
            
            if is_found:
                res = min(res, idx - i)

        return -1 if res == 10 ** 10 else res
    # TLE
    def minMirrorPairDistanceV1(self, nums: List[int]) -> int:
        print(nums)
        rnums = [int(str(num)[::-1]) for num in nums]
        print(rnums)
        n = len(rnums)
        
        res = 10 ** 10
        for i in range(n):
            idx = next((j for j, val in enumerate(nums) if val == rnums[i] and j != i), -1)
            diff = idx - i
            if diff > 0:
                res = min(res, diff)

        return -1 if res == 10 ** 10 else res
    
sol = Solution()
print(sol.minMirrorPairDistance(nums = [12,21,45,33,54]))
print(sol.minMirrorPairDistance(nums = [120,21]))
print(sol.minMirrorPairDistance(nums = [21,120]))
print(sol.minMirrorPairDistance(nums = [9, 9]))