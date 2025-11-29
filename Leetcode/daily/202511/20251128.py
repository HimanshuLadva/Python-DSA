# https://leetcode.com/problems/maximum-number-of-k-divisible-components?envType=daily-question&envId=2025-11-28
# #newlearn

from typing import List
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        self.components = 0
        
        def dfs(node, parent):
            # Calculate sum of current subtree
            subtree_sum = values[node]
            
            # Add sums from all children
            for neighbor in graph[node]:
                if neighbor != parent:
                    subtree_sum += dfs(neighbor, node)
            
            # If subtree sum is divisible by k, we can split it
            if subtree_sum % k == 0:
                self.components += 1
                return 0  # Don't pass this sum to parent
            
            return subtree_sum
        
        dfs(0, -1)
        return self.components