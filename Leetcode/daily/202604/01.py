# https://leetcode.com/problems/robot-collisions/?envType=daily-question&envId=2026-04-01
#newlearn
from typing import List
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if len(set(directions)) == 1:
            return healths

        robots = [(positions[i], healths[i], directions[i], i) for i in range(len(positions))]
        robots.sort(key=lambda x: x[0])
        # print(robots)

        stack = []
        alive = [True] * len(positions)
        healths = healths[:]

        for pos, h, d, idx in robots:
            if d == 'R':
                stack.append(idx)
            else:
                while stack:
                    top = stack[-1]

                    if healths[top] < healths[idx]:
                        alive[top] = False
                        stack.pop()
                        healths[idx] -= 1
                    elif healths[top] > healths[idx]:
                        alive[idx] = False
                        healths[top] -= 1
                        break
                    else:
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break
                else:
                    pass
        
        result = []
        for i in range(len(positions)):
            if alive[i]:
                result.append(healths[i])
        
        return result
    
    def survivedRobotsHealthsV1(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if len(set(list(directions))) == 1:
            return healths

        with_pos = [str(pos)+'#'+directions[i]+'#'+str(healths[i]) for i,pos in enumerate(positions)] 
        with_pos.sort()

        new_positions = []
        new_healths = []
        new_directions = []
        
        for pos in with_pos:
            temp = pos.split("#")
            new_positions.append(temp[0])
            new_directions.append(temp[1])
            new_healths.append(temp[2])

        print(new_positions)
        print(new_healths)
        print(new_directions)
        n = len(with_pos)

        first_i = 0
        result = []
        for i in range(1, n):
            if new_directions[i] != new_directions[first_i]:
                if new_healths[i] != new_healths[first_i]:
                    result.append(int(new_healths[i])-1 if int(new_healths[i]) > int(new_healths[first_i]) else int(new_healths[first_i])-1)
            else:
                first_i = i

        return result

sol = Solution()
# print(sol.survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"))
print(sol.survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"))