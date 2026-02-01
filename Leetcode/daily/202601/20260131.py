# https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType=daily-question&envId=2026-01-31
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        for letter in letters:
            if letter > target:
                res = letter
                break
    
        return res

sol = Solution()
letters = ["c","f","j"]
target = "a"
print(sol.nextGreatestLetter(letters, target))