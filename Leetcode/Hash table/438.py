# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = {}

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        left = 0
        result = []
        window = {}

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if right - left + 1 > len(p):
                left_ch = s[left]
                window[left_ch] -= 1

                if window[left_ch] == 0:
                    del window[left_ch]

                left += 1

            if right - left + 1 == len(p):
                if window == p_count:
                    result.append(left)

        return result

sol = Solution()
sol.findAnagrams(s = "cbaebabacd", p = "abc")