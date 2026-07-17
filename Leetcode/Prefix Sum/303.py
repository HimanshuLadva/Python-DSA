# https://leetcode.com/problems/range-sum-query-immutable/description/
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])


    def sumRange(self, left: int, right: int) -> int:
        # print(f"nums = {self.nums}")
        # print(f"prefix_sum = {self.prefix_sum}")

        if left == 0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))