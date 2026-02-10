# https://leetcode.com/problems/longest-balanced-subarray-i/description/?envType=daily-question&envId=2026-02-10
from typing import List
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            freq = {}
            even_count = 0
            odd_count = 0

            for j in range(i, n):
                x = nums[j]
                if x not in freq:
                    freq[x] = 0
                    if x & 1:
                        odd_count += 1
                    else:
                        even_count += 1
                freq[x] += 1
                
                if odd_count == even_count:
                    ans = max(ans, j - i + 1)
        
        return ans
    # tls
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        for length in range(n, 1, -1):       
            for i in range(n - length + 1):    
                arr = nums[i:i + length] 
                print(arr)
                nums_set = set(arr)
                even_count = sum(1 for x in nums_set if not x & 1)
                odd_count = sum(1 for x in nums_set if x & 1)

                if even_count == odd_count:
                    return len(arr)
        return 0 

        # #implogic - for find all subarray of array
        """ for i in range(n):
            for j in range(i + 1, n + 1):
                arr = nums[i:j] """
        
        # #implogic - for find all subarray of array (big subarray first)
        """ for length in range(n, 0, -1):       
            for i in range(n - length + 1):    
                arr = nums[i:i + length]  """

    
sol = Solution()
nums = [2,5,4,3]
sol.longestBalanced(nums)