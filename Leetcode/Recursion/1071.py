# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

from math import gcd
#howtowork
#revision
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(len(str1), len(str2))]

sol = Solution()
print(sol.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))