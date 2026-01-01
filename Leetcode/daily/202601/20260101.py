# https://leetcode.com/problems/plus-one?envType=daily-question&envId=2026-01-01

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1

        for i in range(len(digits)):
            temp = digits[-i-1] + carry
            if temp > 9:
                carry = 1
                ans.append(0)
            else:
                carry = 0
                ans.append(temp)

        if carry:
            ans.append(1)

        ans.reverse()
        return ans
    
sol = Solution()
digits = [1,2,3]
digits = [4,3,2,1]
digits = [9]
print(sol.plusOne(digits))