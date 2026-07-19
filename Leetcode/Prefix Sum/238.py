# https://leetcode.com/problems/product-of-array-except-self/?envType=problem-list-v2&envId=prefix-sum

from typing import List
class Solution: 
    #revision
    #implogic - finding product of all element except that element
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        return [prefix[i] * suffix[i] for i in range(n)]  
    
    def productExceptSelfV2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # prefix calculation
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i - 1]
        
        # suffix calculation
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # print(prefix, suffix)

        return [prefix[i] * suffix[i] for i in range(n)]


    def productExceptSelfV1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_mul = [nums[0]]
        suffix = [1] * n
        suffix[-1] = nums[-1]

        print(nums, [24,12,8,6])
        for i in range(1, n):
            prefix_mul.append(prefix_mul[-1] * nums[i])
        
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        print(prefix_mul, suffix)
        return []
    
sol = Solution()
# print(sol.productExceptSelf(nums = [1,2,3,4]))
print(sol.productExceptSelf(nums = [-1,1,0,-3,3]))