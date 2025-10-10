# https://leetcode.com/problems/length-of-last-word?envType=problem-list-v2&envId=string

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.strip().split(" ")

        if arr and arr[-1] is not None:
            return len(arr[-1])

        return 0
    
sol = Solution()
s = "Hello World"
s= "   fly me   to   the moon  "
sol.lengthOfLastWord(s)