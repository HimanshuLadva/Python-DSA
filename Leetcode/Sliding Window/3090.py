# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/?envType=daily-question&envId=2026-08-14
#howtowork
#revision
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

sol = Solution()
print(sol.maximumLengthSubstring(s = "bcbbbcba"))