# https://leetcode.com/problems/longest-balanced-substring-ii/description/?envType=daily-question&envId=2026-02-13
from collections import defaultdict
class Solution:
    # #howtowork #revision
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        # Case 1: All 3 characters present with equal frequency
        # Key insight: if count_a - count_b and count_a - count_c are the same
        # at two prefix positions, the substring between them is balanced.
        first = {(0, 0): -1}
        ca = cb = cc = 0
        for i, ch in enumerate(s):
            if ch == 'a':   ca += 1
            elif ch == 'b': cb += 1
            else:           cc += 1
            key = (ca - cb, ca - cc)
            if key in first:
                ans = max(ans, i - first[key])
            else:
                first[key] = i

        # Case 2: Exactly 2 characters with equal frequency (third absent)
        # Split string by the excluded char, then use +1/-1 prefix sum trick
        # abbac
        for exclude, c1, c2 in [('c','a','b'), ('b','a','c'), ('a','b','c')]:
            for seg in s.split(exclude):
                if len(seg) <= ans:
                    continue  # pruning — can't beat current best
                seen = {0: -1}
                balance = 0
                for i, ch in enumerate(seg):
                    balance += 1 if ch == c1 else -1
                    if balance in seen:
                        ans = max(ans, i - seen[balance])
                    else:
                        seen[balance] = i

        # Case 3: Single character only — longest run
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ans = max(ans, j - i)
            i = j

        return ans
    
    # tle
    def longestBalanced(self, s: str) -> int:
        nums = list(s)
        n = len(nums)
        ans = 0

        for i in range(n):
            freq = defaultdict(int)

            for j in range(i, n):
                x = nums[j]
                freq[x] += 1

                vals = [freq['a'], freq['b'], freq['c']]
                non_zero = [v for v in vals if v != 0]

                if len(non_zero) >= 1 and len(set(non_zero)) == 1:
                    ans = max(ans, j - i + 1)

                # print(f"freq = {freq}")
                # print(f"Ans = {ans}")
    
        return ans
    
sol = Solution()
s = "abbac"
print(sol.longestBalanced(s))
