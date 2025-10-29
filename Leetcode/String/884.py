# https://leetcode.com/problems/uncommon-words-from-two-sentences?envType=problem-list-v2&envId=counting

from typing import List
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1 + " " + s2
        arr = s1.split(" ")
        lookup = {}
        for x in arr:
            if x not in lookup:
                lookup[x] = 0
            lookup[x] += 1
        
        result = []
        for x in lookup:
            if lookup[x] == 1:
                result.append(x)
        return result
    
sol = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
sol.uncommonFromSentences(s1, s2)