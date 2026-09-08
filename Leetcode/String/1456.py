# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    #revision
    #implogic
    #howtowork
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        cnt = 0
        ans = 0

        for i in range(len(s)):
            # Add current charecter
            if s[i] in vowels:
                cnt += 1

            if i >= k:
                if s[i - k] in vowels:
                    cnt -= 1

            if i >= k - 1:
                ans = max(ans, cnt)
            
        return ans

    # TLE
    def maxVowelsV1(self, s: str, k: int) -> int:
        vowels = "aeiou"
        ans = 0
        for i in range(len(s) - k + 1):
            window = s[i: i+k]
            cnt = sum(1 for ch in window if ch in vowels)
            ans = max(ans, cnt)
            # print(window)

        return ans

sol = Solution()
print(sol.maxVowels(s = "abciiidef", k = 3))