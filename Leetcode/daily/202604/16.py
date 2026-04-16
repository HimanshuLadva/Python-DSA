# https://leetcode.com/problems/closest-equal-element-queries/?envType=daily-question&envId=2026-04-16
from typing import List
from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # map index
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)

        result = []

        for i in queries:
            target = nums[i]
            idx_list = positions[target]

            if len(idx_list) == 1:
                result.append(-1)
                continue

            # binary search
            pos = bisect.bisect_left(idx_list, i)

            # find neighbors
            left = idx_list[pos - 1] if pos > 0 else idx_list[-1]
            right = idx_list[pos + 1] if pos < len(idx_list) - 1 else idx_list[0]

            # compute circular distance
            left_dist = min(abs(i - left), n - abs(i - left))
            right_dist = min(abs(i - right), n - abs(i - right))

            result.append(min(left_dist, right_dist))
        return result
    # timelimit exceed
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        for startIndex in queries:
            left = (startIndex - 1 + n) % n
            end = (startIndex + n) % n
            right = (startIndex + 1) % n
            
            target = nums[startIndex]
            # for left
            left_count = 0
            is_found = False
            while left != end:
                left_count += 1
                if nums[left] == target:
                    is_found = True
                    break
                left = (left - 1 + n) % n
            
            if not is_found:
                left_count = 0
            
            # for right
            right_count = 0
            is_found = False
            while right != end:
                right_count += 1
                if nums[right] == target:
                    is_found = True
                    break
                right = (right + 1) % n
            
            if not is_found:
                right_count = 0
                
            result.append(-1 if left_count == 0 and right_count == 0 else min(right_count, left_count))
        
        return result
    
sol = Solution()
print(sol.solveQueries(nums = [1,3,1,4,1,3,2], queries = [0,3,5]))
print(sol.solveQueries(nums = [1,2,3,4], queries = [0,1,2,3]))