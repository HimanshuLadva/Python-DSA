# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2026-02-07
#howtowork
class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletion = 0
        b_count = 0

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:
                deletion = min(deletion + 1, b_count)
        return deletion

sol = Solution()
s = "aababbab"
s = "bbaaaaabb"
print(sol.minimumDeletions(s))