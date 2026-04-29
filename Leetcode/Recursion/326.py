# https://leetcode.com/problems/power-of-three/?envType=problem-list-v2&envId=recursion
class Solution:
    def isPowerOfThree(self, n: int, power: int = 0) -> bool:
        if 3**power == n:
            return True
        elif 3**power > n:
            return False

        return self.isPowerOfThree(n, power + 1)        