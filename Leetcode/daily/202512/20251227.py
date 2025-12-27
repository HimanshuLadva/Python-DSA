# https://leetcode.com/problems/meeting-rooms-iii?envType=daily-question&envId=2025-12-27
# #newlearn
import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by original start time
        meetings.sort()
        
        # Min-heap of available rooms (by room number)
        available = list(range(n))
        heapq.heapify(available)
        
        # Min-heap of busy rooms: (end_time, room_number)
        busy = []
        
        # Count meetings per room
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free up rooms that have finished by 'start'
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                # Assign to smallest available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Delay meeting until earliest room is free
                free_time, room = heapq.heappop(busy)
                new_end = free_time + duration
                heapq.heappush(busy, (new_end, room))
            
            count[room] += 1
        
        # Return room with max meetings (tie -> smallest index)
        return count.index(max(count))

    
sol = Solution()
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
sol.mostBooked(n, meetings)
    
