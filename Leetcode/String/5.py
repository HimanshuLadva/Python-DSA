# https://leetcode.com/problems/longest-palindromic-substring/

#howtowork
#revision
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(n):

            # ODD palindrome
            left = right = i

            while left > -1 and right < n and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left: right + 1]

                left -= 1
                right += 1

            # EVEN palindrome
            left = i
            right = i + 1

            while left > -1 and right < n and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left : right + 1]

                left -= 1
                right += 1
            
        return ans

sol = Solution()
# print(sol.longestPalindrome(s = "babad"))
print(sol.longestPalindrome(s = "cbbd"))