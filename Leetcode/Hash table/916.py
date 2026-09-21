# https://leetcode.com/problems/word-subsets/

from collections import Counter
class Solution:
    #howtowork
    #revision
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        required = Counter()

        for word in words2:
            # Take the maximum count for each character.
            required |= Counter(word)

        res = []
        for word in words1:
            curr = Counter(word)
            if curr >= required:
                res.append(word)
            
        return res
    
    # TLE
    def wordSubsetsV1(self, words1: list[str], words2: list[str]) -> list[str]:
        res = []
        
        words2_freq = []
        for word in words2:
            words2_freq.append(Counter(word))

        # print(words2_freq)
        
        for word1 in words1:
            flag = True
            curr = Counter(word1)

            for cnt in words2_freq:
                if (curr & cnt) != cnt:
                    flag = False
                    break

            if flag:
                res.append(word1)

        # print(res)
        return res

sol = Solution()
# print(sol.wordSubsets( words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))
# print(sol.wordSubsets( words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]))
print(sol.wordSubsets( ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]))
# print(sol.wordSubsets( ["amazon","apple","facebook","google","leetcode"], words2 = ["lo","eo"]))