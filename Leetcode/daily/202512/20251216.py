# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts?envType=daily-question&envId=2025-12-16
# #newlearn
from typing import List

class Solution:
    # 405ms
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)
        
        # Iterative Post-order Traversal to avoid recursion depth issues
        stack = [1]
        order = []
        while stack:
            u = stack.pop()
            order.append(u)
            for v in reversed(adj[u]):
                stack.append(v)
        
        # dp[u] will store (f0, f1)
        # f0: array where f0[w] is max profit for subtree u with exact cost w, given parent(u) NOT bought
        # f1: array where f1[w] is max profit for subtree u with exact cost w, given parent(u) IS bought
        dp = [None] * (n + 1)
        
        # Process nodes bottom-up
        for u in reversed(order):
            # Accumulators for children results
            # g0: Sum of profits from children assuming u is NOT bought (so children see unbought parent)
            # g1: Sum of profits from children assuming u IS bought (so children see bought parent)
            g0 = [0]
            g1 = [0]
            
            for v in adj[u]:
                f0_v, f1_v = dp[v]
                dp[v] = None # Free memory
                
                # Convolve g0 with f0_v (Size Optimized Tree Knapsack Merge)
                len_g0, len_f0 = len(g0), len(f0_v)
                new_len = min(budget, len_g0 + len_f0 - 2) + 1
                new_g0 = [-1] * new_len
                
                for i in range(len_g0):
                    if g0[i] == -1: continue
                    limit = min(len_f0, new_len - i)
                    for j in range(limit):
                        if f0_v[j] != -1:
                            val = g0[i] + f0_v[j]
                            if val > new_g0[i + j]:
                                new_g0[i + j] = val
                g0 = new_g0
                
                # Convolve g1 with f1_v
                len_g1, len_f1 = len(g1), len(f1_v)
                new_len = min(budget, len_g1 + len_f1 - 2) + 1
                new_g1 = [-1] * new_len
                
                for i in range(len_g1):
                    if g1[i] == -1: continue
                    limit = min(len_f1, new_len - i)
                    for j in range(limit):
                        if f1_v[j] != -1:
                            val = g1[i] + f1_v[j]
                            if val > new_g1[i + j]:
                                new_g1[i + j] = val
                g1 = new_g1
            
            # Costs and profits for node u
            p_idx = u - 1
            cost_full = present[p_idx]
            prof_full = future[p_idx] - cost_full
            cost_half = cost_full // 2
            prof_half = future[p_idx] - cost_half
            
            len_g0 = len(g0)
            len_g1 = len(g1)
            
            # Calculate f0_u (Parent Unbought)
            # Option 1: Don't buy u. Profit comes from g0.
            # Option 2: Buy u (cost_full). Profit comes from g1 + prof_full.
            len_f0 = min(budget, max(len_g0 - 1, (len_g1 - 1) + cost_full)) + 1
            f0_u = [-1] * len_f0
            
            # Fill Option 1
            for i in range(min(len_f0, len_g0)):
                f0_u[i] = g0[i]
            
            # Fill Option 2
            if cost_full < len_f0:
                limit = min(len_g1, len_f0 - cost_full)
                for i in range(limit):
                    if g1[i] != -1:
                        v = g1[i] + prof_full
                        if v > f0_u[i + cost_full]:
                            f0_u[i + cost_full] = v
            
            # Calculate f1_u (Parent Bought)
            # Option 1: Don't buy u. Profit comes from g0 (children see unbought parent).
            # Option 2: Buy u (cost_half). Profit comes from g1 + prof_half.
            len_f1 = min(budget, max(len_g0 - 1, (len_g1 - 1) + cost_half)) + 1
            f1_u = [-1] * len_f1
            
            # Fill Option 1
            for i in range(min(len_f1, len_g0)):
                f1_u[i] = g0[i]
                
            # Fill Option 2
            if cost_half < len_f1:
                limit = min(len_g1, len_f1 - cost_half)
                for i in range(limit):
                    if g1[i] != -1:
                        v = g1[i] + prof_half
                        if v > f1_u[i + cost_half]:
                            f1_u[i + cost_half] = v
            
            dp[u] = (f0_u, f1_u)
            
        # The answer is max profit at root with parent unbought (virtual parent 0 not bought)
        return max(dp[1][0])
    
    # 9454ms
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        g = [[] for _ in range(n)]
        for e in hierarchy:
            g[e[0] - 1].append(e[1] - 1)

        def dfs(u: int):
            cost = present[u]
            dCost = present[u] // 2

            # dp[u][state][budget]
            # state = 0: Do not purchase parent node, state = 1: Must purchase parent node
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)

            # subProfit[state][budget]
            # state = 0: discount not available, state = 1: discount available
            subProfit0 = [0] * (budget + 1)
            subProfit1 = [0] * (budget + 1)
            uSize = cost

            for v in g[u]:
                child_dp0, child_dp1, vSize = dfs(v)
                uSize += vSize
                for i in range(budget, -1, -1):
                    for sub in range(min(vSize, i) + 1):
                        if i - sub >= 0:
                            subProfit0[i] = max(
                                subProfit0[i],
                                subProfit0[i - sub] + child_dp0[sub],
                            )
                            subProfit1[i] = max(
                                subProfit1[i],
                                subProfit1[i - sub] + child_dp1[sub],
                            )

            for i in range(budget + 1):
                dp0[i] = subProfit0[i]
                dp1[i] = subProfit0[i]
                if i >= dCost:
                    dp1[i] = max(
                        subProfit0[i], subProfit1[i - dCost] + future[u] - dCost
                    )
                if i >= cost:
                    dp0[i] = max(
                        subProfit0[i], subProfit1[i - cost] + future[u] - cost
                    )

            return dp0, dp1, uSize

        return dfs(0)[0][budget]