# https://leetcode.com/problems/valid-word

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'
        vowels += vowels.upper()
        consonants = "bcdfghjklmnpqrstvwxyz"
        consonants += consonants.upper()
        allowed = vowels + consonants + '0123456789'

        if len(word) < 3: return False
        has_vowels = False
        has_consonants = False
        for w in word:
            if w in vowels: has_vowels = True
            if w in consonants: has_consonants = True
            if w not in allowed: return False
        
        return has_vowels and has_consonants