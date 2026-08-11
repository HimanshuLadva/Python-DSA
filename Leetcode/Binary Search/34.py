# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=problem-list-v2&envId=binary-search

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def find_last():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans
        
        return [find_first(), find_last()]
    
sol = Solution()
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))