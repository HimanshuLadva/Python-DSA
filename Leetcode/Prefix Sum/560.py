# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List
from collections import defaultdict
class Solution:
    #implogic
    #revision
    #howtowork
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        count = 0
        running_sum = 0

        # formula: prefix[j] - prefix[i - 1] = k
        # prefix[i-1] = prefix[j] - k

        for num in nums:
            running_sum += num

            count += prefix_map.get(running_sum - k, 0)

            prefix_map[running_sum] += 1

        return count

    def subarraySumV1(self, nums: List[int], k: int) -> int:
        running_sum = 0
        prefix_map = {0: 1}
        count = 0

        for num in nums:
            running_sum += num

            print(running_sum - k)
            print(f"prefix = {prefix_map}")
            if (running_sum - k) in prefix_map:
                count += prefix_map[running_sum - k]

            if running_sum in prefix_map:
                prefix_map[running_sum] += 1
            else:
                prefix_map[running_sum] = 1
            print(f"after prefix = {prefix_map}")

        return count

sol = Solution()
# sol.subarraySum(nums = [1,1,1], k = 2)
# sol.subarraySum(nums = [1,2,3], k = 3)
sol.subarraySum(nums = [1], k = 0)