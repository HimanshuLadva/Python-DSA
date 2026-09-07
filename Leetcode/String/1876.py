# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            window = s[i:i+3]

            if len(window) == len(set(window)):
                count += 1
            
        return count

sol = Solution()
sol.countGoodSubstrings(s = "xyzzaz")