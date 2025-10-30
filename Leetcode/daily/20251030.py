# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array?envType=daily-question&envId=2025-10-30
# #MIMP

from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operation = target[0]
        targetlen = len(target)

        for x in range(1, targetlen):
            if target[x] > target[x - 1]:
                operation += (target[x] - target[x - 1])

        return operation
    
    # brute force approch
    def minNumberOperations(self, target: List[int]) -> int:
        targetlen = len(target)
        initial = [0] * targetlen
        
        count = 0
        while initial != target:
            i = 0
            lays = 0
            while i < targetlen:
                if target[i] == initial[i]:
                    if lays == 1:
                        break
                    i += 1
                elif target[i] > 0 and initial[i] < target[i]:
                    lays = 1
                    initial[i] += 1
                    i += 1
                else:
                    if lays == 1:
                        break
                    i += 1

            count += 1

        return count
    
sol = Solution()
target = [1,2,3,2,1]
target = [3,1,1,2]
target = [3,1,5,4,2]
# target = [1,2,3,4,5]
# target = [0,0,0,0,0]
print(sol.minNumberOperations(target))
        