# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        j = len(s) - 1

        # print(s)
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

sol = Solution()
# sol.isPalindrome(s = "A man, a plan, a canal: Panama")
sol.isPalindrome(s = "0P")