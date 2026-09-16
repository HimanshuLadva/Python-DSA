# https://leetcode.com/problems/subarray-sum-equals-k/description/

#howtowork
#revision
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0:1}

        for num in nums:
            prefix_sum += num
            required = prefix_sum - k

            if required in hashmap:
                count += hashmap[required]

            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count
    
    #TLE
    def subarraySumV1(self, nums: List[int], k: int) -> int:
        n = len(nums)

        count = 0
        for i in range(n):
            for j in range(i+1, n + 1):
                if sum(nums[i:j]) == k:
                    count += 1
                
        return count

sol = Solution()
sol.subarraySum(nums = [1,1,1], k = 2)