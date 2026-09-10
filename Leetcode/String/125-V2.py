# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())

        # print(s)

        n = len(s)
        
        i = 0
        j = 0

        if n % 2 == 0:
            i = (n // 2) - 1
            j = i + 1
        else:
            i = (n // 2)
            j = i

        # print(i, j)

        while i > -1 and j < n:
            if s[i] != s[j]:
                return False

            i -= 1
            j += 1

        return True

sol = Solution()
sol.isPalindrome(s = "A man, a plan, a canal: Panama")
sol.isPalindrome(s = "0P")