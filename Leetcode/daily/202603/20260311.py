# https://leetcode.com/problems/complement-of-base-10-integer/description/?envType=daily-question&envId=2026-03-11

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = format(n, 'b')
        res = ''
        for i in b:
            res += '1' if i == '0' else '0'
    
        return int(res, 2)

sol = Solution()
sol.bitwiseComplement(5)