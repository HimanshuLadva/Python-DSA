# https://leetcode.com/problems/count-special-triplets?envType=daily-question&envId=2025-12-09
from typing import List
from collections import defaultdict,Counter
class Solution:
    #313ms-le
    def specialTriplets(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        pair = defaultdict(int)
        ans = 0
        MOD = 10**9 + 7
        for num in nums:
            if num in counter:
                ans += pair[num] % MOD
            if num * 2 in counter:
                pair[num * 2] += counter[num * 2] % MOD
            counter[num] += 1
        return ans % MOD
    
    # 872ms
    def specialTripletsV1(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        nlen = len(nums)
        count = 0

        left = defaultdict(int)
        right = defaultdict(int)
        for i in range(1, nlen):
            right[nums[i]] += 1

        for j in range(1, nlen-1):
            left[nums[j-1]] += 1

            right[nums[j]] -= 1
            if right[nums[j]] == 0:
                del right[nums[j]]

            mid = nums[j] * 2
            count += left[mid] * right[mid]

        return count % MOD
    
    # TLE
    def specialTripletsV2(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        nlen = len(nums)
        count = 0
        for j in range(1, nlen-1):
            left = Counter(nums[:j])
            right = Counter(nums[j+1:])

            mid = nums[j] * 2
            if mid in left and mid in right:
                count += left[mid] * right[mid]
        return count % MOD
    
    # TLE
    def specialTripletsV1(self, nums: List[int]) -> int:
        nlen = len(nums)
        count = 0
        for i in range(nlen):
            for j in range(i+1, nlen):
                for k in range(j+1, nlen):
                    if nums[j] * 2 == nums[i] == nums[k]:
                        count += 1
        return count
    
sol = Solution()
nums = [0,1,0,0]
nums = [8,4,2,8,4]
nums = [84,2,93,1,2,2,26]
# nums = [6,3,6]
print(sol.specialTriplets(nums))