# Longest Common Prefix
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs, key=len)
        f_str = sorted_strs.pop(0)
        print(f"sorted strings {sorted_strs}")
        ans = ""

        if(len(strs) == 1):
            return strs[0]
        for i,_ in enumerate(f_str):
            count = 0

            print(f"start with {f_str[:i+1]}")
            for str1 in sorted_strs:
                if str1.startswith(f_str[:i+1]):
                    count += 1

            if count == len(sorted_strs):
                ans = f_str[:i+1]

        return ans
    
s = Solution()
# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs = ["a"]
# strs = ["abab","aba","abc"]
strs = ["ab","a"]
result = s.longestCommonPrefix(strs)
print(f"result = {result}")