from typing import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        arr = []

        # replace target with 1 and other with -1
        for num in nums:
            arr.append(1 if num == target else -1)

        # prefix sum
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i+1] = prefix[i] + arr[i]

        count = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if prefix[j] > prefix[i]:
                    count += 1 
        
        # print(prefix)
        return count
        
    # TLE
    def countMajoritySubarraysV1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = nums.count(target)

        for i in range(n):
            for j in range(i+2, n+1):
                temp = nums[i:j]
                apperance = temp.count(target)

                # print(nums[i:j])
                if apperance > ((j - i) // 2):
                    count += 1
        
        return count
    
sol = Solution()
print(sol.countMajoritySubarrays(nums = [1,2,2,3], target = 2))