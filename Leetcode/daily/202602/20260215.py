# https://leetcode.com/problems/add-binary/?envType=daily-question&envId=2026-02-15
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

sol = Solution()
a = "11"
b = "1"
sol.addBinary(a, b)