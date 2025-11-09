# https://leetcode.com/problems/count-operations-to-obtain-zero?envType=daily-question&envId=2025-11-09

class Solution:
    # 0ms
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                count += num1 // num2
                num1 %= num2
            else:
                count += num2 // num1
                num2 %= num1
        return count
    # 39ms
    def countOperationsV1(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        return count
    
sol = Solution()
num1 = 2
num2 = 3
print(sol.countOperations(num1, num2))