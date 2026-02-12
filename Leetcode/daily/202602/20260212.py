# https://leetcode.com/problems/longest-balanced-substring-i/description/?envType=daily-question&envId=2026-02-12

class Solution:
    def longestBalanced(self, s: str) -> int:
        nums = list(s)
        n = len(nums)
        ans = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                x = nums[j]
                if x not in freq:
                    freq[x] = 0
                freq[x] += 1

                if len(set(freq.values())) == 1:
                    ans = max(ans, j - i + 1)

                # print(f"freq = {freq}")
                # print(f"Ans = {ans}")
    
        return ans
    
sol = Solution()
s = "abbac"
sol.longestBalanced(s)