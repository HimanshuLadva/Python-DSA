# Remove element
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # return [x for x in nums if x != val]
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k = k + 1
        return k

s = Solution()
nums = [0,1,2,2,3,0,4,2]
k = s.removeElement(nums, 2)
print(k)
print(nums[:k])