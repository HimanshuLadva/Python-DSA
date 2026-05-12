# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/?envType=daily-question&envId=2026-05-12
#implogic
#revision
from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        for i,(actual, minimum) in enumerate(tasks):
            tasks[i].append(minimum - actual)

        tasks.sort(key=lambda x: x[2], reverse=True)

        answer = 0
        energy = 0
        for actual, minimum, diff in tasks:
            if energy < minimum:
                need = minimum - energy
                answer += need
                energy += need
            
            energy -= actual

        return answer
    
sol = Solution()
# print(sol.minimumEffort(tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]))
print(sol.minimumEffort(tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]))