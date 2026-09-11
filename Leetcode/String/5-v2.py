# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            # odd palindrom
            left = right = i

            while left > -1 and right < n and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left: right + 1]

                left -= 1
                right += 1

            # even palindromn
            left = i
            right = i + 1

            while left > -1 and right < n and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left : right + 1]

                left -= 1
                right += 1

        return ans

sol = Solution()
print(print(sol.longestPalindrome(s = "babad")))