# https://leetcode.com/problems/find-the-duplicate-number/description/

from typing import List
class Solution:
    #howtowork
    #revision
    #implogic
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                slow = nums[0]

                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]

                return slow

sol = Solution()
print(sol.findDuplicate(nums = [1,3,4,2,2]))