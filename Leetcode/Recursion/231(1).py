# https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n: int, ghat:int = 0) -> bool:
        if 2 ** ghat == n:
            return True
        if 2 ** ghat > n:
            return False

        return self.isPowerOfTwo(n, ghat + 1)



        