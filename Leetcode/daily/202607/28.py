# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/?envType=daily-question&envId=2026-07-28

from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        # print(s)
        mid = n // 2

        if n % 2 == 0:
            # print(s[:mid], s[mid:])
            return ''.join(sorted(s[:mid]) + sorted(s[mid:], reverse=True))
        else:
            # print(s[:mid], s[mid+1:])
            return ''.join(sorted(s[:mid]) +[s[mid]] + sorted(s[mid+1:], reverse=True))

sol = Solution()
print(f"answer= {sol.smallestPalindrome(s = "daccad")}")
print(f"answer= {sol.smallestPalindrome(s = "babab")}")