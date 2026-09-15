# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in ransomNote:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False
             
        return True

sol = Solution()
sol.canConstruct(ransomNote = "aa", magazine = "aab")
    