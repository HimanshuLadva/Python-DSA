# Plue One
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d_str = "".join(map(str, digits))
        num = (int(d_str) + 1)  
        return list(map(int, str(num)))    
    
    def plusOnev2(self, digits: List[int]) -> List[int]:
        add_num = 1
        start_index = len(digits) -1
        while start_index >= 0 and add_num == 1:
            if digits[start_index] == 9:
                digits[start_index] = 0

                if start_index == 0 and add_num == 1:
                    digits.insert(0, 1)
                else: 
                    digits[start_index] = 0
                add_num = 1
            else: 
                digits[start_index] += add_num
                add_num = 0
            start_index -= 1
        return digits
    
s = Solution()
# nums = [1,2,3]
# nums = [9]
nums = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
result = s.plusOne(nums)
print(result)