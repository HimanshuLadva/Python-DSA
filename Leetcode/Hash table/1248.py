# https://leetcode.com/problems/count-number-of-nice-subarrays/description/

#revision
#howtowork
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        count = 0
        prefix = 0
        hashmap = {0: 1}

        for num in nums:
            prefix += num

            required = prefix - k

            if required in hashmap:
                count += hashmap[required]

            hashmap[prefix] = hashmap.get(prefix, 0) + 1

        return count

sol = Solution()
sol.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)