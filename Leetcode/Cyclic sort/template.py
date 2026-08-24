# [0, n] example
nums = [3, 6, 0, 1, 5, 2, 7]
n = len(nums)

i = 0
while i < n:
    correct_idx = nums[i]

    if correct_idx < n and nums[i] != nums[correct_idx]:
        nums[i],nums[correct_idx] = nums[correct_idx],nums[i]
    else:
        i += 1

print(nums) # [0, 1, 2, 3, 7, 5, 6]

# [1, n] example
nums2 = [4, 3, 7, 1, 6, 2, 5]
n = len(nums2)

i = 0
while i < n:
    correct_idx = nums2[i] - 1

    if correct_idx < n and nums2[i] != nums2[correct_idx]:
        nums2[i], nums2[correct_idx] = nums2[correct_idx], nums2[i]
    else:
        i += 1

print(nums2) # [1, 2, 3, 4, 5, 6, 7]