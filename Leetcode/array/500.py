# https://leetcode.com/problems/keyboard-row/?envType=problem-list-v2&envId=array
from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        ans = []
        for word in words:
            if all(ch in first_row for ch in word.lower()):
                ans.append(word)
            elif all(ch in second_row for ch in word.lower()):
                ans.append(word)
            elif all(ch in third_row for ch in word.lower()):
                ans.append(word)

        return ans

sol = Solution()
print(sol.findWords(words = ["Hello","Alaska","Dad","Peace"]))