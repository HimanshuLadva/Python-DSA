# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = len(blocks)
        for i in range(len(blocks) - k + 1):
            window = blocks[i: i+k]
            ans = min(ans, window.count('W'))
            # print(window)
        return ans

sol = Solution()
# print(sol.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
print(sol.minimumRecolors(blocks = "WBWW", k = 2))