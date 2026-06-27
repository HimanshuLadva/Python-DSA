# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/submissions/2046986371/?envType=daily-question&envId=2026-06-26

from typing import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # hint-1: Convert to +1/-1: let arr[i] = 1 if nums[i] == target else -1.
        arr = [1 if x == target else -1 for x in nums]

        # hint-2: Build prefix sums: pref[0]=0, pref[k] = pref[k - 1] + arr[k - 1] for k=1..n.
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        # hint-4 Use coordinate compression on all pref values and a Fenwick tree / ordered map: iterate k from 0..n, query how many previous pref are < current, add to ans, then update.
        vals = sorted(set(prefix))
        rank = {}
        for i, v in enumerate(vals):
            rank[v] = i + 1
        
        
        return 0
    
sol = Solution()
sol.countMajoritySubarrays(nums = [1,2,2,3], target = 2)