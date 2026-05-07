# https://leetcode.com/problems/jump-game-ix/?envType=daily-question&envId=2026-05-07

from typing import List
class Solution:
    def maxValueV1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_value = max(nums)
        max_value_idx = nums.index(max_value)
        ans = []

        # print(f"max_value_idx = {max_value_idx}, n = {n}")
        if max_value_idx == n-1:
            for i in range(n):
                # print(f"max = {max(nums[:i+1])}")
                ans.append(max(nums[:i+1]))
        else:
            ans = [max_value] * n

        return ans
    
    def maxValue(self, nums: List[int]) -> List[int]:
        print(f"org_nums = {nums}")
        n = len(nums)
        ans = []

        for i in range(n):
            # right direction j > i && nums[j] < nums[i]
            right_max = nums[i]
            right_idx = i

            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    right_max = min(nums[j], right_max)
                    right_idx = j

            # left direction j < i && nums[j] > nums[i]
            print(f"right_max = {right_max}, right_idx = {right_idx}")
            left_max = nums[i]

            for j in range(right_idx-1,-1,-1):
                # if nums[j] > nums[i]:
                if nums[j] > nums[right_idx]:
                    left_max = max(nums[j], left_max)

            print(f"left_max = {left_max}, right_idx = {right_idx}")
            print("--------------------------------")

            ans.append(max(left_max, right_max))

        return ans

sol = Solution()
# print(sol.maxValue([2,1,3]))
# print(sol.maxValue([4,1,3,2,5]))
# print(sol.maxValue([11,18,11, 2]))
print(sol.maxValue([30,21,5,35,24]))