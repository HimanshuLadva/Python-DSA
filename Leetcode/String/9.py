# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        n = len(temp)
        i = 0
        j = 0

        if n % 2 == 0:
            i = (n // 2) - 1
            j = i + 1
        else:
            i = (n // 2)
            j = i

        print(i, j)

        while i > -1 and j < n:
            if temp[i] != temp[j]:
                return False

            i -= 1
            j += 1

        return True

sol = Solution()
sol.isPalindrome(x = 1212)