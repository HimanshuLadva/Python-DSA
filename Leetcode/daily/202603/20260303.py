# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=daily-question&envId=2026-03-03
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(1, n):
            old_s = s
            inverted = ''.join('1' if c == '0' else '0' for c in s)
            r_inverted = ''.join(reversed(inverted))
            s = old_s + '1' + r_inverted

        # print(f"str = {s}")
        return s[k-1]
    
sol = Solution()
print(sol.findKthBit(4, 11))