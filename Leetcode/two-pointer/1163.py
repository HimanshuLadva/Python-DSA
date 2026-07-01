# https://leetcode.com/problems/last-substring-in-lexicographical-order/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)

        res = s[:n]
        for i in range(n):
            temp = s[i:n]
            if temp > res:
                res = temp

        # print(res) 
        return res
    
sol = Solution()
sol.lastSubstring(s = "leetcode")