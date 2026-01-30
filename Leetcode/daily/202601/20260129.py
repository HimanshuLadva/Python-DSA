# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=daily-question&envId=2026-01-29
#newlearn
from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], 
                    changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        
        # Initialize distance matrix for 26 letters
        dist = [[INF] * 26 for _ in range(26)]
        
        # Distance from a character to itself is 0
        for i in range(26):
            dist[i][i] = 0
        
        # Build graph: add edges with minimum cost
        for i in range(len(original)):
            from_idx = ord(original[i]) - ord('a')
            to_idx = ord(changed[i]) - ord('a')
            dist[from_idx][to_idx] = min(dist[from_idx][to_idx], cost[i])
        
        # Floyd-Warshall: find all shortest paths
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate total conversion cost
        total_cost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                from_idx = ord(source[i]) - ord('a')
                to_idx = ord(target[i]) - ord('a')
                
                if dist[from_idx][to_idx] == INF:
                    return -1  # Impossible to convert
                
                total_cost += dist[from_idx][to_idx]
        
        return total_cost
        