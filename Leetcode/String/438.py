# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List
class Solution:
    #revision
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        ans = []
        p_count = [0] * 26
        window_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - 97] += 1

        for i in range(n):
            window_count[ord(s[i]) - 97] += 1

        if window_count == p_count:
            ans.append(0)
    

        for i in range(n, len(s)):
            window_count[ord(s[i]) - 97] += 1
            window_count[ord(s[i - n]) - 97] -= 1

            if window_count == p_count:
                ans.append(i - n + 1)

        return ans

    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        ans = []
        p = "".join(sorted(p))

        for i in range(len(s) - n + 1):
            window = s[i: i+n]

            if p == "".join(sorted(window)):
                ans.append(i)

            # print(window)

        return ans

sol = Solution()
print(sol.findAnagrams(s = "cbaebabacd", p = "abc"))