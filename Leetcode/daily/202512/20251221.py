# https://leetcode.com/problems/delete-columns-to-make-sorted-ii?envType=daily-question&envId=2025-12-21
# #newlearn
from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n <= 1:
            return 0
        
        m = len(strs[0])
        # sorted_pairs[i] = True means strs[i] < strs[i+1] is already established
        sorted_pairs = [False] * (n - 1)
        deletions = 0
        
        for col in range(m):
            # Check if this column creates any violations
            # among pairs that aren't already sorted
            has_violation = False
            
            for i in range(n - 1):
                if not sorted_pairs[i]:  # Only check unsorted pairs
                    if strs[i][col] > strs[i + 1][col]:
                        has_violation = True
                        break
            
            if has_violation:
                # Delete this column
                deletions += 1
            else:
                # Keep this column and update sorted pairs
                for i in range(n - 1):
                    if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                        sorted_pairs[i] = True
            
            # Early termination: if all pairs are sorted, we're done
            if all(sorted_pairs):
                break
        
        return deletions
    
sol = Solution()
strs = ["ca","bb","ac"]
strs = ["xc","yb","za"]
strs = ["xga","xfb","yfa"]
print(sol.minDeletionSize(strs))