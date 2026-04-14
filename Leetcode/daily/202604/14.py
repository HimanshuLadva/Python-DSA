# https://leetcode.com/problems/minimum-total-distance-traveled/description/?envType=daily-question&envId=2026-04-14
#newlearn
#learntopic -dp
from typing import List
class Solution:
    # fromeditorial
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.sort()
        factories.sort()

        factory_positions = []
        for factory in factories:
            for i in range(factory[1]):
                factory_positions.append(factory[0])

        robot_count = len(robots)
        factory_count = len(factory_positions)
        next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]

        current[factory_count] = 1e12

        for i in range(robot_count - 1, -1, -1):
            for j in range(factory_count - 1, -1, -1):
                assign = (abs(robots[i] - factory_positions[j]) + next_dist[j + 1])

                skip = current[j + 1]

                current[j] = min(assign, skip)

            next_dist = current[:]

        return current[0]
    # 32 of 40 test passed
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        ans = 0
        result = []
        
        print(f"robots = {robot}")
        print(f"factory = {factory}")

        for r in robot:
            min_distance = float('inf')
            idx = 0
            for i,(position,limit) in enumerate(factory):
                dist = abs(position - r)
                if dist < min_distance and limit > 0:
                    min_distance = dist
                    idx = i

            if factory[idx][1] > 0:
                factory[idx][1] -= 1
                ans += min_distance
                result.append((r, factory[idx][0]))
                if factory[idx][1] == 0:
                    factory.pop(idx)

        print(result)

        return ans
    
sol = Solution()
# print(sol.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]]))
print(sol.minimumTotalDistance(robot = [9,11,99,101], factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]))