# https://leetcode.com/problems/valid-parentheses?envType=problem-list-v2&envId=string
# #pending
class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for x in s:
            result.append(x)
            if x == ')' and '(' in result:
                result = []
            if x == ']' and '[' in result:
                result = []
            if x == '}' and '{' in result:
                result = []

        print(f"result = {result}")

        if len(result) != 0:
            return False

        return True
    
sol = Solution()
s = "()[]{}"
s = "([])"
print(sol.isValid(s))