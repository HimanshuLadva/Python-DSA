# https://leetcode.com/problems/valid-parentheses/?envType=problem-list-v2&envId=wyg0cz82

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(',']':'[','}':'{'}

        for x in s:
            if x in pairs:
                if not stack or stack.pop() != pairs[x]:
                    return False
            else:
                stack.append(x)

        # print(f"len = {len(stack)}")
        return len(stack) == 0

sol = Solution()
print(sol.isValid(s = "()[]{[{[]}]}"))