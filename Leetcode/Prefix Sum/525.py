from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        first = {0:-1}
        n = len(nums)
        max_len = 0

        for i in range(n):
            if nums[i] == 0:
                balance -= 1
            else:
                balance += 1

            if balance in first:
                max_len = max(max_len, i - first[balance])
            else:
                first[balance] = i

        return max_len

sol = Solution()
print(sol.findMaxLength(nums = [0,1,1,1,1,1,0,0,0]))
# print(sol.findMaxLength(nums = [0,1,0]))
        