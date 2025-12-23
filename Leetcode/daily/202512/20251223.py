# https://leetcode.com/problems/two-best-non-overlapping-events?envType=daily-question&envId=2025-12-23
# #Xms-le
from typing import List
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        starts = sorted(events)
        ends = sorted(events, key=lambda x: x[1])
        i = 0
        best_before = 0
        result = 0
        for start, end, value in starts:
            while ends[i][1] < start:
                best_before = max(best_before, ends[i][2])
                i += 1
            result = max(result, best_before + value)
        return result
    
    # TLE
    def maxTwoEventsV1(self, events: List[List[int]]) -> int:
        def ranges_overlap(range1, range2):
            return range1[1] >= range2[0] and range2[1] >= range1[0]
        
        n = len(events)
        ans = set()
        for i in range(n):
            ans.add(events[i][2])
            for j in range(n):
                if i == j:
                    continue
                
                if not ranges_overlap(events[i], events[j]):
                    ans.add(events[i][2] + events[j][2])

        return max(ans)
        
    
sol = Solution()
events = [[1,3,2],[4,5,2],[2,4,3]]
events = [[1,3,2],[4,5,2],[1,5,5]]
events = [[1,5,3],[1,5,1],[6,6,5]]
print(sol.maxTwoEvents(events))