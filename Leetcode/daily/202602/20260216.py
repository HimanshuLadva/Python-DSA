# https://leetcode.com/problems/reverse-bits/?envType=daily-question&envId=2026-02-16
class Solution:
    #howtowork
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n = n >> 1
        return result

    def reverseBits(self, n: int) -> int:
        b = format(n, '032b')
        reversed_b = b[::-1]
        return int(reversed_b, 2)
        
sol = Solution()
n = 43261596
print(sol.reverseBits(n))