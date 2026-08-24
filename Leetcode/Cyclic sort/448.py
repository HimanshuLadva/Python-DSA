from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0
        while i < n:
            correct_idx = nums[i] - 1

            if correct_idx < n and nums[i] != nums[correct_idx]:
                nums[i],nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # print(nums)
        ans = []
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)

        return ans

sol = Solution()
print(sol.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))