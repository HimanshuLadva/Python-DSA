# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings?envType=daily-question&envId=2026-01-10
# #newlearn
# #learntopic
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def solve(i, j):
            # if one string is finished, delete all remaining chars of the other
            if i == len(s1):
                return sum(ord(c) for c in s2[j:])
            if j == len(s2):
                return sum(ord(c) for c in s1[i:])

            # if characters match, keep them (no cost)
            if s1[i] == s2[j]:
                return solve(i + 1, j + 1)

            # otherwise, delete from either s1 or s2
            delete_s1 = ord(s1[i]) + solve(i + 1, j)
            delete_s2 = ord(s2[j]) + solve(i, j + 1)

            return min(delete_s1, delete_s2)

        return solve(0, 0)

sol = Solution()
s1 = "delete"
s2 = "leet"
print(sol.minimumDeleteSum(s1, s2))