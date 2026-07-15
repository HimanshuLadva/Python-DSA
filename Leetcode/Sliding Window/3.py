# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=sliding-window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0

        for right in range(len(s) + 1):
            temp = s[left: right]

            print(temp, left,right)
            if len(temp) != len(set(temp)):
                left += 1
            else:
                max_len = max(max_len, right - left)

        return max_len
    # TLE
    def lengthOfLongestSubstringV1(self, s: str) -> int:
        n = len(s)

        max_len = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                temp = s[i:j]
                temp_len = len(temp)

                if len(temp) == len(set(temp)):
                    max_len = max(max_len, temp_len)
        
        return max_len
    
sol = Solution()
# print(sol.lengthOfLongestSubstring(s = "abcabcbb"))
# print(sol.lengthOfLongestSubstring(s = "pwwkew"))
# print(sol.lengthOfLongestSubstring(s = "au"))
print(sol.lengthOfLongestSubstring(s = "aab"))