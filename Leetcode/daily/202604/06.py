# https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2026-04-06
from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set((obstacle[0],obstacle[1]) for obstacle in obstacles)
        x_dir = [0, 1, 0, -1]
        y_dir = [1, 0, -1, 0]
        dir = 0
        x = 0
        y = 0
        res = 0
        for cmd in commands:
            if cmd == -2:
                dir = (dir + 3) % 4
            elif cmd == -1:
                dir = (dir + 1) % 4
            else:
                for i in range(cmd):
                    newX = x + x_dir[dir]
                    newY = y + y_dir[dir]
                    if (newX, newY) not in obs:
                        x = newX
                        y = newY
                        res = max(res, x*x+y*y)
                    else:
                        break
        return res