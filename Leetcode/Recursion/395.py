# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#revision
#howtowork
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = Counter(s)

        for ch,n in count.items():
            if n < k:
                return max(self.longestSubstring(x, k) for x in s.split(ch))

        return len(s)

sol = Solution()
sol.longestSubstring(s = "ababbc", k = 2)