# https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]

        if abs(b.count('0')) - abs(b.count('1')) > 1:
            return False

        last_bit = -1
        for i in n:
            if last_bit == i:
                return False
            last_bit = i
             
        return True
    def hasAlternatingBits(self, n: int) -> bool:
        b = list(bin(n)[2:])

        for i in range(len(b) - 1):
            if b[i] == b[i+1]:
                return False
        
        return True

sol = Solution()
sol.hasAlternatingBits(21)