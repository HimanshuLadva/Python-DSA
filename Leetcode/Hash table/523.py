# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    #implogic
    #revision
    #howtowork
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        prefix = 0
        hashmap = {0:-1}
        left = 0

        for right in range(n):
            prefix += nums[right]

            required = prefix % k

            #formula: If two prefix  sums have the same remainder when divided by k, the elements between them have a sum divisible by k.
            if required in hashmap:
                left = hashmap[required]

                if right - left >= 2:
                    return True
            else:
                hashmap[required] = right

        return False

sol = Solution()
sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6)