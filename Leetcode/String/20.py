# https://leetcode.com/problems/valid-parentheses?envType=problem-list-v2&envId=string

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        result = []
        for x in s:
            if x in ['(','[','{']:
                result.append(x)
            else:
                top = result[-1] if len(result) > 0 else ''
                if top == '(' and x == ')': 
                    result.pop()
                elif top == '[' and x == ']':
                    result.pop()
                elif top == '{' and x == '}':
                    result.pop()
                else:
                    return False

        # print(f"result = {result}")

        if len(result) != 0:
            return False

        return True
    
sol = Solution()
s = "()[]{}"
# s = "([])"
s = ")(){}"
print(sol.isValid(s))