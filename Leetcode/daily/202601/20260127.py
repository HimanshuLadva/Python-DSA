# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/?envType=daily-question&envId=2026-01-27
#newlearn
from typing import List
from math import inf
import heapq
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, 2 * w))

        dist = [inf] * n
        visited = [False] * n
        dist[0] = 0
        heap = [(0, 0)]  # (Distance, Node)

        while heap:
            cur_dist, x = heapq.heappop(heap)

            if x == n - 1:
                return cur_dist

            # already processed
            if visited[x]:
                continue
            visited[x] = True

            # relaxing neighbors
            for y, w in g[x]:
                new_dist = cur_dist + w
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(heap, (new_dist, y))

        return -1

sol = Solution()
n = 4
edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
sol.minCost(n, edges)