# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        #implogic
        s1 = "01" * (n // 2) + "0" * (n % 2)
        s2 = "10" * (n // 2) + "1" * (n % 2)
        count = 0
        count2 = 0
        for i in range(n):
            if s[i] != s1[i]:
                count += 1
            if s[i] != s2[i]:
                count2 += 1

        return min(count, count2)
    
sol = Solution()
s = "10010101001"
sol.minOperations(s)