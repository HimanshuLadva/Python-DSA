# https://leetcode.com/problems/find-the-string-with-lcp/description/?envType=daily-question&envId=2026-03-28
#newlearn
from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        # Step 1: DSU (Union-Find)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Step 2: Union indices where lcp[i][j] > 0
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)
        
        # Step 3: Assign characters
        group_char = {}
        curr_char = ord('a')
        res = [''] * n
        
        for i in range(n):
            root = find(i)
            if root not in group_char:
                if curr_char > ord('z'):
                    return ""  # more than 26 groups → impossible
                group_char[root] = chr(curr_char)
                curr_char += 1
            res[i] = group_char[root]
        
        word = "".join(res)
        
        # Step 4: Validate LCP matrix
        dp = [[0] * n for _ in range(n)]
        
        # compute LCP from bottom-right
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i == n - 1 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 0
        
        # compare with given lcp
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word