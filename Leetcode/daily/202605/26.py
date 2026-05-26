# https://leetcode.com/problems/count-the-number-of-special-characters-i/description/?envType=daily-question&envId=2026-05-26
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper_word = {x.lower() for x in word if x.isupper()}
        lower_word = {x for x in word if x.islower()}

        return len(upper_word & lower_word)
    
    # 3ms
    def numberOfSpecialChars(self, word: str) -> int:
        words = set([x for x in word if x.isupper()])
        # print(words) 
        
        count = 0
        for x in words:
            if x.lower() in word:
                count += 1
        return count

sol = Solution()
print(sol.numberOfSpecialChars(word = "aaAbcBC"))
print(sol.numberOfSpecialChars(word = "CCc"))