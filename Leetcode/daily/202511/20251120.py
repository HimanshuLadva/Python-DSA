# https://leetcode.com/problems/set-intersection-size-at-least-two?envType=daily-question&envId=2025-11-20
# #newlearn-topic-bisect_left or right

from typing import List
from bisect import bisect_left,bisect_right
class Solution:
    # 10ms
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1]))
        result = []
        for interval in intervals:
            start,end = interval
            l = bisect_left(result, start)
            r = bisect_right(result, end)
            c = r - l

            if c >= 2: continue
            elif c == 1:
                if end not in result:
                    result.append(end)
                else:
                    result = result[:-1] + [end - 1, end]
            else:
                result += [end-1, end]
            
        return len(result)
    
    # 90ms
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        result = set()
        for interval in intervals:
            start,end = interval[0],interval[1]

            count = 0
            for num in result:
                if start <= num <= end:
                    count += 1
                    if count == 2:
                        break
            
            if count == 0:
                result.add(end)
                result.add(end - 1)
            elif count == 1:
                if end not in result:
                    result.add(end)
                else:
                    result.add(end - 1)
            
        return len(result)
    # memory limit exceeded
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        result = set()
        for interval in intervals:
            temp = [x for x in range(interval[0], interval[1]+1)]
            if len(result) == 0:
                result.add(temp[-1])
                result.add(temp[-2])
            else:
                count = 0
                for x in temp:
                    if x in result:
                        count +=1
                    if count == 2:
                        break
                
                if count == 0:
                    result.add(temp[-1])
                    result.add(temp[-2])
                elif count == 1:
                    if temp[-1] not in result:
                        result.add(temp[-1])
                    else:
                        result.add(temp[-2])

        return len(result)
    
sol = Solution()
# intervals = [[4,5], [5,9], [9,10], [7,9], [1,5]]
intervals = [[1,3],[1,4],[2,5],[3,5]]
sol.intersectionSizeTwo(intervals)