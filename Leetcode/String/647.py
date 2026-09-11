# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0

        for i in range(n):
            # odd palindrom
            left = right = i

            while left > -1 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1

            # even palindromn
            left = i
            right = i + 1

            while left > -1 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1

        return cnt

sol = Solution()
print(sol.countSubstrings(s = "aaa"))