# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        seen = set()

        for i, num in enumerate(nums):
            x = num
            # target = x + y + z
            lookup = {}
            for j in range(i+1, len(nums)):
                num1 = nums[j]

                if 0 - x - num1 in lookup:
                    # print(f"ddd = {[x,0 - x - num1,num1]}")
                    seen.add((x,0 - x - num1,num1))

                lookup[num1] = j

        # print(seen)
        return [[x,y,z] for x,y,z in seen]

sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))