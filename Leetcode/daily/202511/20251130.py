# https://leetcode.com/problems/make-sum-divisible-by-p?envType=daily-question&envId=2025-11-30
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        
        # Already divisible by p
        if target == 0:
            return 0
        
        # Dictionary to store last index where each remainder was seen
        # mod_dict[r] = last index where prefix_sum % p = r
        mod_dict = {0: -1}  # Empty prefix has remainder 0 at index -1
        
        curr_sum = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            curr_sum += num
            curr_mod = curr_sum % p
            
            # We need to find a prefix with remainder = (curr_mod - target) % p
            needed = (curr_mod - target + p) % p
            
            # If we found such a prefix, calculate subarray length
            if needed in mod_dict:
                min_len = min(min_len, i - mod_dict[needed])
            
            # Update the dictionary with current remainder's index
            mod_dict[curr_mod] = i
        
        # If min_len is still n, we couldn't find valid subarray
        return min_len if min_len < len(nums) else -1