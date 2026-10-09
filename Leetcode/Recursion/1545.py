# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/

class Solution:
    def findKthBit(self, n: int, k: int, s:str = '0') -> str:
        # print(f"str = {s}")
        if n == 0:
            return s[k-1]
        old_s = s
        inverted = "".join('1' if ch == '0' else '0' for ch in s)
        s = old_s + '1' + ''.join(reversed(inverted))

        return self.findKthBit(n-1, k, s)

    def findKthBitV1(self, n: int, k: int) -> str:
        s = "0"

        for i in range(1, n):
            old_s = s
            inverted = "".join('1' if ch == '0' else '1' for ch in s)
            s = old_s + '1' + ''.join(reversed(inverted))

        return s[k-1]

sol = Solution()
print(sol.findKthBit(n = 3, k = 1))
print(sol.findKthBit(n = 4, k = 11))
print(sol.findKthBit(n = 3, k = 5))