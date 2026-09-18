# https://leetcode.com/problems/group-anagrams/description/

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            key = tuple(sorted(str))

            if key not in hashmap:
                hashmap[key] = [str]
            else:
                hashmap[key].append(str)

        # print(hashmap.values())
        return list(hashmap.values())

sol = Solution()
sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])