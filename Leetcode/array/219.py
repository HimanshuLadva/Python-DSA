# https://leetcode.com/problems/contains-duplicate-ii/?envType=problem-list-v2&envId=array

from typing import List
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = defaultdict(list)

        for i, num in enumerate(nums):
            lookup[num].append(i)

        for key, value in lookup.items():
            n = len(value)
            if n > 1:
                print(key, value)
                i = 0
                j = 1

                while j < n:
                    if abs(value[i] - value[j]) <= k:
                        return True
                    i += 1
                    j += 1


        return False
    
sol = Solution()
sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)