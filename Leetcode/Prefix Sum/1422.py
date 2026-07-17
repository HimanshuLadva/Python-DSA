# https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=problem-list-v2&envId=prefix-sum

class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            # print(f"{s[:i+1]}, {s[i+1:]}")
            temp = s[:i+1].count('0') + s[i+1:].count('1')
            ans = max(temp, ans)

        return ans
    
sol = Solution()
sol.maxScore(s = "011101")