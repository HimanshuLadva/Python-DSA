# https://leetcode.com/problems/power-grid-maintenance?envType=daily-question&envId=2025-11-06
# #newlearn
from typing import List
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Step 1: Build Union-Find to group stations into connected components (grids)
        parent = list(range(c + 1))  # parent[i] = parent of station i
        
        def find(x):
            """Find the root parent of station x with path compression"""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Unite two stations into the same grid"""
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        # Connect all stations based on connections
        for u, v in connections:
            union(u, v)
        
        # Step 2: Group stations by their grid (connected component)
        from collections import defaultdict
        import heapq
        
        grids = defaultdict(list)  # grids[root] = list of stations in that grid
        
        for station in range(1, c + 1):
            root = find(station)
            grids[root].append(station)
        
        # Step 3: Create a min-heap for each grid to track online stations
        grid_heaps = {}  # grid_heaps[root] = min-heap of online stations in that grid
        
        for root, stations in grids.items():
            # Create a min-heap with all stations (all start online)
            grid_heaps[root] = stations.copy()
            heapq.heapify(grid_heaps[root])
        
        # Step 4: Track which stations are offline
        offline = set()  # Set of offline station IDs
        
        # Step 5: Process queries
        result = []
        
        for query in queries:
            query_type = query[0]
            station = query[1]
            
            if query_type == 1:  # Maintenance check
                if station not in offline:
                    # Station is online, handles its own check
                    result.append(station)
                else:
                    # Station is offline, find smallest online station in same grid
                    root = find(station)
                    heap = grid_heaps[root]
                    
                    # Remove offline stations from top of heap (lazy deletion)
                    while heap and heap[0] in offline:
                        heapq.heappop(heap)
                    
                    if heap:
                        # Found an online station
                        result.append(heap[0])
                    else:
                        # No online stations in this grid
                        result.append(-1)
            
            else:  # query_type == 2, station goes offline
                offline.add(station)
        
        return result
    # not completed
    def processQueriesV1(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # getting query point
        qpoint = set(x[1] for x in queries)
        print(qpoint)

        power_grid = {}
        temp = set()
        for x in connections:
            print(f"x[0] = {x[0]}, x[1] = {x[1]}")
            if x[0] not in temp and x[1] not in temp:
                if len(temp):
                    sorted_set = sorted(temp)
                    power_grid[(sorted_set[0],sorted_set[-1])] = sorted_set
                    temp.clear() 
            
            temp.add(x[0])
            temp.add(x[1])
        
        if len(temp):
            sorted_set = sorted(temp)
            power_grid[(sorted_set[0],sorted_set[-1])] = sorted_set

        print(power_grid)

        # for query
        for x in queries:
            if x[0] == 2:
                power_grid.get()
        return [[]]
    
sol = Solution()
c = 5 # 1,2,3,4,5
connections = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
sol.processQueries(c, connections, queries)