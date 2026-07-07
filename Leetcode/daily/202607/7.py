# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/?envType=daily-question&envId=2026-07-07

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = "0"
        sum_s = 0
        for ch in str(n):
            if ch != "0":
                res += ch
                sum_s += int(ch)
        
        return int(res) * sum_s