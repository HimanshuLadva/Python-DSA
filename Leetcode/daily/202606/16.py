# https://leetcode.com/problems/process-string-with-special-operations-i/?envType=daily-question&envId=2026-06-16

class Solution:    
    def processStr(self, s: str) -> str:
        res = ""
        
        for ch in s:
            if ch == '#':
                res += res
            elif ch == '%':
                res = res[::-1]
            elif ch == '*':
                res = res[:-1]
            else:
                res += ch
            
        return res
    
sol = Solution()
sol.processStr(s = "a#b%*")