# https://leetcode.com/problems/3sum?envType=problem-list-v2&envId=two-pointers

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nlen = len(nums)
        nums.sort()
        ans = []

        for k in range(nlen):
            if k > 0 and nums[k] == nums[k-1]:
                continue

            i = k+1
            j = nlen - 1

            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif s < 0:
                    i += 1
                else:
                    j -= 1

        return ans
    
    def threeSumV1(self, nums: List[int]) -> List[List[int]]:
        nlen = len(nums)
        i = 0
        j = nlen - 1
        ans = set()

        while i < j:
            for k in range(nlen):
                if nums[i] + nums[j] + nums[k] == 0 and (i != j and j != k and i != k):
                    ans.add(tuple(sorted((nums[i], nums[j], nums[k]))))
            # if abs(nums[i]) > abs(nums[j]):
            if nums[i] > nums[j]:
                i += 1
            else:
                j -= 1

        return [list(x) for x in ans]
    
sol = Solution()
nums = [-1,0,1,2,-1,-4]
nums = [1,2,-2,-1]
nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
print(sol.threeSum(nums))