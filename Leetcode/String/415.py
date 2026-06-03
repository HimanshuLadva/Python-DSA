# https://leetcode.com/problems/add-strings/description/?envType=problem-list-v2&envId=string

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0

            total = x + y + carry
            result.append(str(total % 10))
            carry = total // 10 

            i -= 1
            j -= 1
        return "".join(reversed(result))
    
sol = Solution()
print(sol.addStrings(num1 = "11", num2 = "123"))