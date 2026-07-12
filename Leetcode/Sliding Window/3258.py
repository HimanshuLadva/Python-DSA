# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/description/?envType=problem-list-v2&envId=sliding-window
#howtowork
#revision
#implogic - this is sliding window problem without fixed size window
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0
        cnt0 = 0
        cnt1 = 0
        ans = 0

        for right in range(len(s)):
            if s[right] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
            
            while cnt0 > k and cnt1 > k:
                if s[left] == '0':
                    cnt0 -= 1
                else:
                    cnt1 -= 1
                left += 1
            
            ans += right - left + 1
        return ans
    
sol = Solution()
print(sol.countKConstraintSubstrings(s = "10101", k = 1))