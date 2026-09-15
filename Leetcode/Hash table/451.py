# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        arr = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        ans = ""

        # print(freq, arr)
        for ch in arr:
            ans += ch * freq[ch]

        return ans

sol = Solution()
# print(sol.frequencySort(s = "Aabb"))
print(sol.frequencySort(s = "tree"))