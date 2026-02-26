# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2026-02-26
class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        count = 0

        while n != 1:
            if n & 1 == 0:
                n //= 2
            else:
                n += 1
            count += 1

        return count