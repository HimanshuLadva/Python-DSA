# https://leetcode.com/problems/binary-gap/?envType=daily-question&envId=2026-02-22

class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        # print(f"bin = {b}")
        diff = None
        ans = 0
        for i,x in enumerate(b):
            if x == '1':
                if diff!=None and i - diff > ans:
                    # print(f"i = {i}, diff = {diff}")
                    ans = i - diff
                diff = i
        # print(f"diff = {ans}")
        return ans
    
sol = Solution()
sol.binaryGap(22)
# sol.binaryGap(15)