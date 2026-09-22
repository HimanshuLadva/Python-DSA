# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # target = a + b + c + d
        nums.sort()
        seen = set()

        for i,a in enumerate(nums):

            for j in range(i+1, len(nums)):
                b = nums[j]
                lookup = {}

                for k in range(j+1, len(nums)):
                    c = nums[k]
                    if target - a - b - c in lookup:
                        # print([a,b,target-a-b-c,c])
                        seen.add((a,b,target-a-b-c,c))

                    lookup[c] = k

        return [[a,b,c,d] for a,b,c,d in seen] 

sol = Solution()
print(sol.fourSum(nums = [1,0,-1,0,-2,2], target = 0))       