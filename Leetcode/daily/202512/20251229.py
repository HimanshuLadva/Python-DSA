# https://leetcode.com/problems/pyramid-transition-matrix?envType=daily-question&envId=2025-12-29
# #newlearn
from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build lookup: pair -> set of possible tops
        lookup = defaultdict(set)
        for a in allowed:
            lookup[a[:2]].add(a[2])

        memo = {}

        def dfs(row: str) -> bool:
            # If we reached the top
            if len(row) == 1:
                return True

            if row in memo:
                return memo[row]

            # Generate all possible next rows
            def build_next(i: int, curr: str):
                if i == len(row) - 1:
                    yield curr
                    return

                pair = row[i:i+2]
                if pair not in lookup:
                    return

                for ch in lookup[pair]:
                    yield from build_next(i + 1, curr + ch)

            for next_row in build_next(0, ""):
                if dfs(next_row):
                    memo[row] = True
                    return True

            memo[row] = False
            return False

        return dfs(bottom)

    # running till 62 testcase
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        lookup = {}
        for a in allowed:
            if a[:2] not in lookup:
                lookup[a[:2]] = ""
            lookup[a[:2]]= a[2]
        
        # print(f"lookup = {lookup}")
        n = len(bottom)
        next = bottom
        i = n-1
        # print(f"start = {next}")
        while i > 0:
            temp = ""
            for j in range(i):
                if next[j:j+2] in lookup:
                    temp += lookup[next[j:j+2]]
                # print(f"stage = {temp}, {j}")
            # print(f"middle = {temp}, {i}")
            if len(temp) == i:
                next = temp
            else:
                return False
            i -= 1

        # print(lookup)
        return True

sol = Solution()
bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]
bottom = "ABCD"
allowed = ["ABC","BCA","CDA","ABD","BCE","CDF","DEA","EFF","AFF"]
print(sol.pyramidTransition(bottom, allowed))