# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        left = 0
        window = {}
        for right in range(len(s2)):
            ch = s2[right]

            window[ch] = window.get(ch, 0) + 1

            if right - left + 1 > len(s1):
                left_ch = s2[left]
                window[left_ch] -= 1

                if window[left_ch] == 0:
                    del window[left_ch]

                left += 1

            if right - left + 1 == len(s1):
                if window == s1_count:
                    return True

        return False

sol = Solution()
sol.checkInclusion(s1 = "ab", s2 = "eidbaooo")