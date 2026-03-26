# https://leetcode.com/problems/equal-sum-grid-partition-ii/description/?envType=daily-question&envId=2026-03-26
#newlearn
from typing import List
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        for _ in range(4):
            exist = set()
            exist.add(0)
            sum_val = 0
            m = len(grid)
            n = len(grid[0])
            if m < 2:
                grid = self.rotation(grid)
                continue
            if n == 1:
                for i in range(m - 1):
                    sum_val += grid[i][0]
                    tag = sum_val * 2 - total
                    if tag == 0 or tag == grid[0][0] or tag == grid[i][0]:
                        return True
                grid = self.rotation(grid)
                continue
            for i in range(m - 1):
                for j in range(n):
                    exist.add(grid[i][j])
                    sum_val += grid[i][j]
                tag = sum_val * 2 - total
                if i == 0:
                    if tag == 0 or tag == grid[0][0] or tag == grid[0][n - 1]:
                        return True
                    continue
                if tag in exist:
                    return True
            grid = self.rotation(grid)
        return False

    def rotation(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        tmp = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                tmp[j][m - 1 - i] = grid[i][j]
        return tmp
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        for use_rows in [True, False]:
            if use_rows:
                total_sum = [sum(row) for row in grid]
                total_arr = grid
            else:
                total_sum = [sum(col) for col in zip(*grid)]
                total_arr = list(zip(*grid))
            
            prefix = 0
            for i in range(len(total_sum) - 1):
                prefix += total_sum[i]
                suffix = sum(total_sum) - prefix

                if prefix == suffix:
                    return True
                
                diff = abs(prefix - suffix)

                if prefix > suffix:
                    for j in range(i+1):
                        if diff in total_arr[j]:
                            return True
                else:
                    for j in range(i+1, len(total_arr)):
                        if diff in total_arr[j]:
                            return True
        return False
    # wrong approch
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        print(f"stage-1 = {grid}")
        if m % 2 == 0:
            total_sum = list(sum(row) for row in grid)
            total_arr = list(row for row in grid)
        else:
            total_sum = list(sum(col) for col in zip(*grid))
            total_arr = list(col for col in zip(*grid))

        print(f"stage-2 = {total_sum}, {total_arr}")

        i = 0
        first_section = 0
        while i < len(total_sum) // 2:
            first_section += total_sum[i]
            i += 1
        
        second_section = 0
        while i < len(total_sum):
            second_section += total_sum[i]
            i += 1
        
        print(f"stage-3 {first_section}, {second_section}")
        if first_section == second_section:
            print("stage-4")
            return True
        
        diff = 0
        if first_section > second_section:
            diff = first_section - second_section
            print(f"stage-5 {diff} {total_arr[0]}")
            if diff in total_arr[0]:
                return True
        else:
            diff = second_section - first_section
            print(f"stage-5 {diff} {total_arr[1]}")
            if len(total_arr) > 1 and diff in total_arr[1]:
                return True

        return False
    
sol = Solution()
# print(sol.canPartitionGrid(grid = [[1,2],[3,4]]))
print(sol.canPartitionGrid([[73816],[71688]]))