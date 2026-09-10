# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word:str):
            n = len(word)
            i = 0
            j = 0
    
            if n % 2 == 0:
                i = (n // 2) - 1
                j = i + 1
            else:
                i = (n // 2)
                j = i
    
            # print(i, j)
    
            while i > -1 and j < n:
                if word[i] != word[j]:
                    return False
    
                i -= 1
                j += 1
    
            return True

        for word in words:
            if isPalindrome(word):
                return word

        return ""

sol = Solution()
sol.firstPalindrome(words = ["abc","car","ada","racecar","cool"])