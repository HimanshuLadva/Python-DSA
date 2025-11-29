from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # return sum([x%k for x in nums]) % k
        return sum(nums) % k
        for num in nums:
            num = num % k
            print(num % k)
        print("--------------------------")
        print(sum(nums) % k)
        return 0
    
sol = Solution()
nums = [3,9,7]
k = 5
# nums = [4,1,3]
# k = 4
# nums = [3,2]
# k = 6
# nums = [1,2,3,4,5]
# k = 2
sol.minOperations(nums, k)