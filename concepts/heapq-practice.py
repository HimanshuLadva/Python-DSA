import heapq as hp

nums = [4, 1, 7, 3, 8, 5]
max_heap = [-x for x in nums]

hp.heapify(max_heap)
print(max_heap)