#  Number of Excellent Pairs
import bisect

class Solution:
    def countExcellentPairs(self, nums, k):
        # Step 1: remove duplicates
        nums = list(set(nums))
        
        # Step 2: precompute bit counts
        counts = [bin(x).count("1") for x in nums]
        counts.sort()
        
        # Step 3: count pairs
        ans = 0
        n = len(counts)
        
        for c in counts:
            # Need c' >= k - c
            idx = bisect.bisect_left(counts, k - c)
            ans += (n - idx)
        
        return ans
