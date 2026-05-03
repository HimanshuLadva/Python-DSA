# https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2026-05-03

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        res = s+s
        if goal in res:
            return True
        return False
    # 1ms
    def rotateStringV1(self, s: str, goal: str) -> bool:
        goal_arr = list(goal)
        s_arr = list(s)
        n = len(s_arr)

        for i in range(n):
            s_arr.insert(0, s_arr.pop())

            if s_arr == goal_arr:
                return True
        return False        
    
sol = Solution()
print(sol.rotateString(s = "abcde", goal = "cdeab"))