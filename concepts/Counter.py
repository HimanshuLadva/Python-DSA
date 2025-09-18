from collections import Counter

s = "abcdabcdxyz"
result = Counter(s)
print(result)

arr = [1,1,3,4,5,6,7,3,4]
result = Counter(arr)
print(result)

matrix = [[1,2],[2,3],[1,2],[3,4],[5,6],[2,3]]
result = Counter(tuple(row) for row in matrix)
print(result)