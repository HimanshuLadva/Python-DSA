# https://leetcode.com/problems/process-string-with-special-operations-ii/description/?envType=daily-question&envId=2026-06-17

class Solution:  
    #howtowork
    #implogic
    #revision
    def processStr(self, s: str, k: int) -> str:
        length = 0

        for c in s:
            if c == "*":
                if length:
                    length -= 1
            elif c == "#":
                length *= 2
            elif c == "%":
                pass
            else:
                length += 1

        if k+1 > length:
            return "."

        for c in reversed(s):
            if c == "*":
                length += 1

            elif c == "#":
                length //= 2
                if k >= length: 
                    k -= length

            elif c == "%":
                k = length - k - 1

            else:
                length -= 1
                if k == length:
                    return c
                
        return '.'
    
    # getting MLE error
    def processStr(self, s: str, k: int) -> str:
        res = []
        
        for ch in s:
            n = len(res)
            if ch == '#':
                res += res
            elif ch == '%':
                res.reverse()
            elif ch == '*':
                if n > 0:
                    res.pop()
            else:
                res.append(ch)
            
        return res[k] if len(res)-1 >= k else '.' 