nums = [1,2,3,4]
n = len(nums)
print(f"Main Array = {nums}")

# prefix sum
prefix_sum = [nums[0]]
for i in range(1, n):
    prefix_sum.append(prefix_sum[-1] + nums[i])

# method 2
prefix_sum = [0] * n
prefix_sum[0] = nums[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i]

print(prefix_sum)

# suffix sum
suffix_sum = [0] * n 
suffix_sum[-1] = nums[-1]
for i in range(n-2, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + nums[i]

print(suffix_sum)

# prefix sum except current element
prefix_sum = [0] * n
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

print(prefix_sum)

# suffix sum except current element
suffix_sum = [0] * n
for i in range(n-2,-1,-1):
    suffix_sum[i] = suffix_sum[i + 1] + nums[i + 1]

print(suffix_sum)