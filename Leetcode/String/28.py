# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        n = len(haystack)

        for right in range(1, n+1):
            window = haystack[left: right]
            # print(window)

            if window == needle:
                return left

            while right - left+1 > len(needle):
                left += 1

        return -1

sol = Solution()
print(sol.strStr(haystack = "saxdbutsad", needle = "sad"))
print(sol.strStr(haystack = "leetcode", needle = "leeto"))
