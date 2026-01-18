# https://leetcode.com/problems/largest-magic-square/description/?envType=daily-question&envId=2026-01-18
#revision - need to revision method of how to find all submatrix of matrix
#learntopic - prefix sum
from typing import List
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # prefix sums
        row_ps = [[0] * (C + 1) for _ in range(R)]
        col_ps = [[0] * C for _ in range(R + 1)]
        diag1 = [[0] * (C + 1) for _ in range(R + 1)]
        diag2 = [[0] * (C + 2) for _ in range(R + 1)]

        for i in range(R):
            for j in range(C):
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j]
                col_ps[i + 1][j] = col_ps[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def is_magic(i, j, k):
            target = row_ps[i][j + k] - row_ps[i][j]

            # rows
            for r in range(i, i + k):
                if row_ps[r][j + k] - row_ps[r][j] != target:
                    return False

            # columns
            for c in range(j, j + k):
                if col_ps[i + k][c] - col_ps[i][c] != target:
                    return False

            # diagonals
            if diag1[i + k][j + k] - diag1[i][j] != target:
                return False
            if diag2[i + k][j] - diag2[i][j + k] != target:
                return False

            return True

        largest = 1
        for size in range(2, min(R, C) + 1):
            for i in range(R - size + 1):
                for j in range(C - size + 1):
                    if is_magic(i, j, size):
                        largest = size

        return largest

    # 9729 ms
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        max_size = min(R, C)

        largest = 1
        # find all submatrix of matrix
        for size in range(2, max_size + 1):        # square size
            for i in range(R - size + 1):           # start row
                for j in range(C - size + 1):       # start col
                    # print(f"Square {count} ({size}x{size}):")
                    # print(f"row = {list(range(i,i+size))},col = {list(range(j, j+size))}")

                    # row sums
                    row_sums = set(sum(grid[i + r][j:j+size]) for r in range(size))

                    # col sums
                    col_sums = set(
                        sum(grid[i + r][j + c] for r in range(size))
                        for c in range(size)
                    )

                    if len(row_sums) != 1 or len(col_sums) != 1:
                        continue

                    diag1 = sum(grid[i + d][j + d] for d in range(size))
                    diag2 = sum(grid[i + d][j + size - 1 - d] for d in range(size))
                    r_sum = row_sums.pop()
                    c_sum = col_sums.pop()

                    if r_sum == c_sum == diag1 == diag2 and size > largest:
                        largest = size

                    # for r in range(i, i + size):
                    #     print(grid[r][j:j + size])

                    # print()
        return largest
    
sol = Solution()
grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
print(sol.largestMagicSquare(grid))