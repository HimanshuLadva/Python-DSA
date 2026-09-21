# https://leetcode.com/problems/determine-if-two-strings-are-close/

#revision
#howtowork
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word2) > len(word1):
            return False

        freq1 = {}
        freq2 = {}

        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1

        # print(freq1.keys(), freq2.keys())
        # the frequencies can move between characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # print(freq1.values(), freq2.values())
        # set of characters must remain the same
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False
        
        return True

sol = Solution()
print(sol.closeStrings(word1 = "cabbba", word2 = "abbccc"))