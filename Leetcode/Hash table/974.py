# https://leetcode.com/problems/subarray-sums-divisible-by-k/

#revision
#howtowork
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        hashmap = {0: 1}

        # print(f"Main array = {nums}, k = {k}")
        for num in nums:
            prefix_sum += num
            required = prefix_sum % k
            # print(f"required = {required}")

            if required in hashmap:
                count += hashmap[required]

            # print(f"before = {hashmap}, {prefix_sum}, {prefix_sum % k}")
            hashmap[prefix_sum % k] = hashmap.get(prefix_sum % k, 0) + 1
            # print(f"after = {hashmap}")
            # print('--------------------')

        return count

sol = Solution()
sol.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5)        