sample = [[0] * 6 for i in range(3)]
for i in range(3):
    for j in range(6):
        print((i,j), end=" ")
    print()

matrix = [[1,2,3]
          ,[4,5,6]
          ,[7,8,9]]

def traverse(matrix):
    if not matrix:
        return []
    
    m, n = len(matrix), len(matrix[0])
    top,bottom = 0, m - 1
    left,right = 0, n - 1

    result = []

    while top <= bottom and left <= right:
        # 1. left -> right (bottom row)
        for col in range(left, right + 1):
            result.append(matrix[bottom][col])
        bottom -= 1

        # 2. bottom -> top (right column)
        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # 3. right -> left (top row)
            for col in range(right, left - 1, -1):
                result.append(matrix[top][col])
            top += 1
        
        if left <= right:
            # 4. top -> bottom (left column)
            for row in range(top, bottom + 1):
                result.append(matrix[row][left])
            left += 1

    return result

result = traverse(matrix)
print(result)

# find position after k step
def find_position(m, n, k):
    top,left = 0,0
    bottom,right = m - 1, n - 1

    while True:
        height = bottom - top + 1
        width = right - left + 1

        # single row
        if height == 1:
            return (bottom, left + k)
        
        # single column
        if width == 1:
            return (bottom - k, left)
        
        perimeter = 2 * (width + height) - 4

        if k < perimeter:
            break

        k -= perimeter
        top += 1
        bottom -= 1
        left += 1
        right -= 1
    
    # bottom row
    if k < width:
        return (bottom, left + k)
    k -= width

    # right column
    if k < height - 1:
        return (bottom - 1 - k, right)
    k -= (height - 1)

    # top row
    if k < width - 1:
        return (top, right - 1 - k)
    k -= (width - 1)

    # left column
    return (top + 1 + k, left)

print(find_position(3, 6, 6))