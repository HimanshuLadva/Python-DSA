# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        ans = 0

        for right in range(n+1):
            window = s[left: right]

            if len(window) != len(set(window)):
                left += 1
            else:
                ans = max(right - left, ans)

        return ans        