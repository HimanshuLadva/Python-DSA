# https://leetcode.com/problems/unique-length-3-palindromic-subsequences?envType=daily-question&envId=2025-11-21

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        lookup = {}
        for i,x in enumerate(s):
            if x not in lookup:
                lookup[x] = []
            lookup[x].append(i)
        
        count = 0
        for x in lookup:
            if len(lookup[x]) > 1:
                temp = lookup[x]
                count += len(set(s[temp[0]+1:temp[-1]]))
        return count