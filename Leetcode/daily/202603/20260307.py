# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/?envType=daily-question&envId=2026-03-07
#newlearn
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        alt1 = ""
        alt2 = ""
        
        for i in range(2*n):
            if i % 2:
                alt1 += "1"
                alt2 += "0"
            else:
                alt1 += "0"
                alt2 += "1"
        
        res = float('inf')
        diff1 = diff2 = 0
        l = 0
        
        for r in range(2*n):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
            
            if r - l + 1 > n:
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1
            
            if r - l + 1 == n:
                res = min(res, diff1, diff2)
        
        return res