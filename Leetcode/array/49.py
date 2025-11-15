from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for str in strs:
            s_sorted = sorted(str)
            key = tuple(s_sorted)
            if key not in ans:
                ans[key] = [str]
            else:
                ans[key].append(str)
        return ans.values()

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))   