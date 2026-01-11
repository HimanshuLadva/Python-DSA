# https://leetcode.com/problems/roman-to-integer?envType=problem-list-v2&envId=hash-table
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        n = len(s)
        i = 0

        while i < n - 1:
            if roman[s[i]] < roman[s[i+1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
            i += 1
        ans += roman[s[i]]

        return ans
    # 3ms
    def romanToInt(self, s: str) -> int:
        lookup = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        n = len(s)
        i = 0

        # print(f"start = {s}")
        while i < n:
            match s[i]:
                case 'I':
                    if i + 1 < n and s[i+1] in ['V', 'X']:
                        ans += lookup[s[i+1]] - lookup[s[i]]
                        i += 1
                    else:
                        ans += lookup[s[i]]
                case 'X':
                    if i + 1 < n and s[i+1] in ['L', 'C']:
                        ans += lookup[s[i+1]] - lookup[s[i]]
                        i += 1
                    else:
                        ans += lookup[s[i]]
                case 'C':
                    if i + 1 < n and s[i+1] in ['D', 'M']:
                        ans += lookup[s[i+1]] - lookup[s[i]]
                        i += 1
                    else:
                        ans += lookup[s[i]]
                case _:
                    ans += lookup[s[i]]
            i += 1
        return ans
        
    
sol = Solution()
s = "LVIII"
# s = "MCMXCIV"
s = "IV"
print(sol.romanToInt(s))