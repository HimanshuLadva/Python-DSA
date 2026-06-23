# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split(" ")])
    
sol = Solution()
sol.reverseWords(s = "Let's take LeetCode contest")