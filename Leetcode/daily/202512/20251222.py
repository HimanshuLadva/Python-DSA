# https://leetcode.com/problems/delete-columns-to-make-sorted-iii?envType=daily-question&envId=2025-12-22
# #newlearn

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # dp[j] = longest valid sequence ending at column j
        dp = [1] * m
        max_keep = 1

        for j in range(m):
            for i in range(j):
                if self.can_extend(strs, i, j):
                    dp[j] = max(dp[j], dp[i] + 1)
            max_keep = max(max_keep, dp[j])

        return m - max_keep

    def can_extend(self, strs: List[str], i: int, j: int) -> bool:
        for s in strs:
            if s[i] > s[j]:
                return False
        return True
