# https://leetcode.com/problems/special-binary-string/description/?envType=daily-question&envId=2026-02-20
#newlogin #howtowork
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def solve(s):
            if len(s) <= 2:
                return s
            
            balance = 0
            start = 0
            str_list = []
            for i,x in enumerate(s):
                
                if x == '1':
                    balance += 1
                else:
                    balance -= 1

                if balance == 0:
                    inner = s[start+1:i]
                    processed_inner = solve(inner)
                    str_list.append("1"+processed_inner+'0')
                    start = i + 1
            
            str_list.sort(reverse=True)

            return "".join(str_list)
        
        return solve(s)
    
sol = Solution()
s = "11011000"
sol.makeLargestSpecial(s)