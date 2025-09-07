""" 
When to use this technique
=> The problem involves a contiguous sequence (subarray or substring).
=> You need to find:
    => Maximum/Minimum sum in a fixed-size window.
    => Longest/Shortest subarray with certain conditions.
    => Count of distinct elements in a range.

How to Identify Sliding Window Problems?
=> These problems generally require finding maximum/minimum subarray,substrings which satisfy
some specific condition
=> The size of the subarray or substring ‘k’ will be given in some of the problems.
=> Required time complexity: O(n) or O(n log n)
=> Constaints: n <= 10^6
"""

# Maximum Sum of a Subarray with K Elements

def maxSumSubarray(nums: list[int], k:int) -> int:
    n = len(nums)
    print(f"length = {n}")

    if n < k:
        print("Invalid input!!")
        return -1
    
    window_sum = sum(nums[:k])

    max_sum = window_sum

    for i in range(n - k):
        # window_sum = window_sum - arr[i] + arr[i+k]
        subarray = nums[i+1: i+k+1]
        window_sum = sum(subarray)
        max_sum = max(window_sum, max_sum)
        print(f"sub array = {subarray}, i = {i}")

    return max_sum

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(maxSumSubarray(arr, k))
