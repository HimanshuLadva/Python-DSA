# https://leetcode.com/problems/valid-palindrome?envType=problem-list-v2&envId=two-pointers
from typing import List

# optimization pending
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(x.lower() for x in s if x.isalnum())
        i = 0
        j = len(s)-1

        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        return True

s = Solution()
str = "A man, a plan, a canal: Panama"
# str = "race a car"
print(s.isPalindrome(str))