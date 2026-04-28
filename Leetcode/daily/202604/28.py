# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/?envType=daily-question&envId=2026-04-28

from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [x for row in grid for x in row]
        arr.sort()
        # print(arr)

        n = len(arr)
        mid = (n // 2) - 1 if n & 1 == 0 else n // 2
        # print(arr[mid])
        target = arr[mid]

        op_count = 0
        for num in arr:
            if num != target:
                diff = abs(target - num)
                diff2 = (target - num)
                if diff // x == 0:
                    return -1
                
                sub = int(diff // x)
                
                # print(f"for num = {num}, diff = {diff2} oppp = {diff // x} new_num = {num - (x * sub)} ,sub = {sub}")
                if (diff2 > 0 and (num + (x * sub)) == target) or (diff2 < 0 and (num - (x * sub)) == target):
                    op_count += abs(diff // x)
                else:
                    return -1
            
        return op_count
    
sol = Solution()
print(sol.minOperations(grid = [[2,4],[6,8]], x = 2))
print(sol.minOperations(grid = [[1,5],[2,3]], x = 1))
print(sol.minOperations(grid = [[1,2],[1,2]], x = 2))
print(sol.minOperations(grid = [[4],[1]], x = 2))
