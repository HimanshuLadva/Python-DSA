# https://leetcode.com/problems/first-unique-character-in-a-string?envType=problem-list-v2&envId=counting

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for x in counter:
            if counter[x] == 1:
                return s.index(x)
        return -1
    
sol = Solution()
# s = "loveleetcode"
s = "leetcode"
sol.firstUniqChar(s)