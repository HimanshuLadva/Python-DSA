# https://leetcode.com/problems/words-within-two-edits-of-dictionary/?envType=daily-question&envId=2026-04-22
from typing import List
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries)
        m = len(dictionary)

        bk_queries = queries[:]
        temp_arr = []
        
        for i in range(n):
            for j in range(m):
                diff = sum(1 for x, y in zip(queries[i], dictionary[j]) if x != y)
                # print(f"que = {queries[i]}, dict = {dictionary[j]}, diff = {diff}")
                if diff <= 2 and queries[i] in bk_queries:
                    bk_queries[i] = ""
                    # print(f"bk = {bk_queries}")
                    temp_arr.append(queries[i])
                    break
        
        # print(f"temp_arr = {temp_arr}")
        return temp_arr
    
sol = Solution()
# print(sol.twoEditWords(queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]))
print(sol.twoEditWords(queries = ["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"], dictionary = ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"]))
# print(sol.twoEditWords(queries = ["t","i","m","i","p","s"], dictionary = ["w","j","b","p","u","b","u","i","h","m"]))