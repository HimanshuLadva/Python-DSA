# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i?envType=daily-question&envId=2025-10-23

class Solution:
    def hasSameDigits(self, s: str) -> bool:
      result = ""
      temp = s
      while len(result) != 2:
        result = ""
        for i in range(1, len(temp)):
            result += str((int(temp[i-1]) + int(temp[i])) % 10)

        temp = result

      if result[0] != result[1]:
        return False
      
      return True
      
    
sol = Solution()
s = "34789"
s = "3902"
print(sol.hasSameDigits(s))