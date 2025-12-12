# https://leetcode.com/problems/count-mentions-per-user?envType=daily-question&envId=2025-12-12
# #newlearn
from typing import List

class Solution:
    def countMentions(
        self,
        numberOfUsers: int,
        events: List[List[str]]
    ) -> List[int]:
        # Sort events by timestamp, and ensure OFFLINE events come before MESSAGE at same time
        def sort_key(e):
            # e[1] is timestamp; event type OFFLINE has higher priority (0) than MESSAGE (1)
            return (int(e[1]), 0 if e[0] == "OFFLINE" else 1)
        
        events.sort(key=sort_key)
        
        # Track mention counts and when each user returns online
        ans = [0] * numberOfUsers
        next_online = [0] * numberOfUsers
        lazy_all = 0
        
        for etype, ts, data in events:
            t = int(ts)
            
            if etype == "OFFLINE":
                # User goes offline until t+60
                user_id = int(data)
                next_online[user_id] = t + 60
            else:
                # MESSAGE
                if data == "ALL":
                    # Lazy increment
                    lazy_all += 1
                elif data == "HERE":
                    # Only count online users
                    for u in range(numberOfUsers):
                        if next_online[u] <= t:
                            ans[u] += 1
                else:
                    # Specific ids (may include duplicates like "id0 id0")
                    tokens = data.split()
                    for tok in tokens:
                        uid = int(tok[2:])
                        ans[uid] += 1
        
        # Add lazy ALL mentions to all users
        if lazy_all:
            for i in range(numberOfUsers):
                ans[i] += lazy_all
        
        return ans
