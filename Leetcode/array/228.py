# https://leetcode.com/problems/summary-ranges/description/?envType=problem-list-v2&envId=array

from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        diff = []
        prev = set()

        for i in range(n):
            if i + 1 < n and nums[i+1] - nums[i] == 1:
                prev.add(nums[i])
                prev.add(nums[i+1])
            else:
                prev.add(nums[i])
                min_p = min(prev)
                max_p = max(prev)

                if min_p == max_p:
                    diff.append(f"{min_p}")
                else:
                    diff.append(f"{min_p}->{max_p}")
                prev.clear()
        
        return diff

sol = Solution()
# sol.summaryRanges(nums = [0,2,3,4,6,8,9])
sol.summaryRanges(nums = [0,1,2,4,5,7])
