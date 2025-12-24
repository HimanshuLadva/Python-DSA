n = 3
matrix = [[0] * n for i in range(n)]
print(matrix)
# how to solve this kind of question
for i in range(n):
    for j in range(n):
        print(f"{i, j} ",end=" ")
    print()

""" 
Core Matrix Traversal Patterns
1. Simple Traversals
Row-by-row (standard nested loop)
Column-by-column
Diagonal traversal (both directions)
Spiral traversal (clockwise/counterclockwise)
Snake/zigzag traversal

2. Direction Arrays
directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]  # 8 directions

Used for: navigating neighbors, BFS/DFS in grids
3. In-Place Modifications
Rotate matrix (transpose + reverse rows/columns)
Flip matrix (horizontal/vertical)
Modify using constant space by marking visited cells 
"""