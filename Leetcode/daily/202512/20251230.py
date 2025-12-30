# https://leetcode.com/problems/magic-squares-in-grid?envType=daily-question&envId=2025-12-30
from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        result=0

        if rows<3 or cols<3:
            return 0

        for i in range(rows-2):
            for j in range(cols-2):
                #consider grid[i][j] as the start of hte grid and compute
                #current grid is going to be from 
                """
                grid[i][j]      grid[i][j+1]     grid[i][j+2]
                grid[i+1][j]    grid[i+1][j+1]   grid[i+1][j+2]
                grid[i+2][j]    grid[i+2][j+1]   grid[i+2][j+2]
                """
                #in this current grid, we have to find if its the one we look for
                store=set()
                invalid=False
                for a in range(3):
                    for b in range(3):
                        current=grid[i+a][j+b]

                        store.add(current)

                        if current>9 or current<1:
                            invalid=True
                            break

                if len(store)!=9:
                    continue

                if invalid:
                    continue

                firstcol=grid[i][j] + grid[i][j+1] + grid[i][j+2]
                secondcol=grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
                firstrow=grid[i][j] + grid[i+1][j] + grid[i+2][j]
                secondrow=grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
                thirdcol=grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                firstdiagonal=grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                thirdrow= grid[i][j+2] +  grid[i+1][j+2] + grid[i+2][j+2]
                seconddiagonal=grid[i+1][j+1] + grid[i+2][j] + grid[i][j+2]
                
                if firstcol==secondcol==firstrow==secondrow==thirdcol==firstdiagonal==thirdrow==seconddiagonal:
                    result+=1

        return result

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m < 3 or n < 3:
            return 0
        
        count = 0
        for row in range(m-2):
            for col in range(n-2):
                store = set()
                Invalid = False

                for i in range(3):
                    for j in range(3):
                        current = grid[row+i][col+j]
                        
                        store.add(current)
                        if current > 9 or current < 1:
                            Invalid = True
                            break
                
                if Invalid:
                    continue
                
                if len(store) != 9:
                    continue

                """
                grid[row][col]      grid[row][col+1]     grid[row][col+2]
                grid[row+1][col]    grid[row+1][col+1]   grid[row+1][col+2]
                grid[row+2][col]    grid[row+2][col+1]   grid[row+2][col+2]
                """
                firstcol=grid[row][col] + grid[row+1][col] + grid[row+2][col]
                secondcol=grid[row][col+1]+grid[row+1][col+1]+grid[row+2][col+1]
                thirdcol=grid[row][col+2]+grid[row+1][col+2]+grid[row+2][col+2]

                firstrow=grid[row][col]+grid[row][col+1]+grid[row][col+2]
                secondrow=grid[row+1][col]+grid[row+1][col+1]+grid[row+1][col+2]
                thirdrow=grid[row+2][col]+grid[row+2][col+1]+grid[row+2][col+2]

                l_diag = grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]
                r_diag = grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col]

                if firstcol==secondcol==firstrow==secondrow==thirdcol==l_diag==thirdrow==r_diag:
                    count += 1

        return count
    def numMagicSquaresInsideV1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # print(f"m = {m}, n = {n}")
        if m < 3 or n < 3:
            return 0
        
        def is_valid_3x3(matrix):
            return {num for row in matrix for num in row} == set(range(1, 10))

        
        count = 0
        for row in range(m-2):
            for col in range(n-2):
                submatrix = [
                    [grid[row][col],grid[row][col+1],grid[row][col+2]],
                    [grid[row+1][col],grid[row+1][col+1],grid[row+1][col+2]],
                    [grid[row+2][col],grid[row+2][col+1],grid[row+2][col+2]]
                ]

                if not is_valid_3x3(submatrix):
                    continue

                row_sum = {sum(submatrix[0]),sum(submatrix[1]),sum(submatrix[2])}
                # print(f"row_sum = {row_sum}")

                col_sum = {
                    submatrix[0][0] + submatrix[1][0] + submatrix[2][0],
                    submatrix[0][1] + submatrix[1][1] + submatrix[2][1],
                    submatrix[0][2] + submatrix[1][2] + submatrix[2][2]
                }
                # print(f"col_sum = {col_sum}")

                left_diagonal = submatrix[0][0] + submatrix[1][1] + submatrix[2][2]
                # print(f"left_diagonal = {left_diagonal}")

                right_diagonal = submatrix[0][2] + submatrix[1][1] + submatrix[2][0]
                # print(f"right_diagonal = {right_diagonal}")

                x = row_sum.pop()
                y = col_sum.pop()
                if len(row_sum) == len(col_sum) == 0 and x == y == left_diagonal == right_diagonal:
                    count += 1

        return count

sol = Solution()
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
grid = [[4,7,8],[9,5,1],[2,3,6]]
grid = [[8,1,6],[3,5,7],[4,9,2]]
# grid = [[4,3,8,4,5],[9,5,1,9,10],[2,7,6,2,10],[2,7,6,2,10]]
print(sol.numMagicSquaresInside(grid))