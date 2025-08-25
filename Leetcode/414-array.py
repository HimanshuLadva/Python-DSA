# https://leetcode.com/problems/third-maximum-number?envType=problem-list-v2&envId=array
# Third Maximum Number
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f_max = s_max = t_max = float('-inf')

        for num in nums:
            if num > f_max:
                t_max = s_max
                s_max = f_max
                f_max = num
            elif num > s_max and num != f_max:
                t_max = s_max
                s_max = num
            elif num > t_max and num != f_max and num != s_max:
                t_max = num

        if t_max == float('-inf'):
            return f_max
        return t_max


              
    def thirdMaxV1(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums), reverse=True)
        if len(sorted_nums) > 2:
            return sorted_nums[2]
        else:
            return sorted_nums[0]        
    
s = Solution()
nums = [3,2,1]
print(s.thirdMax(nums))