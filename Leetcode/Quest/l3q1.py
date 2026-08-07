# https://leetcode.com/problems/build-an-array-with-stack-operations/?envType=problem-list-v2&envId=dsa-linear-shoal-stack

from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        temp = []

        for i in range(1, n+1):
            if temp == target:
                break
            temp.append(i)
            if i in target:
                ans.append("Push")
            else:
                temp.pop()
                ans.append("Push")
                ans.append("Pop")
        return ans

sol = Solution()
print(sol.buildArray(target = [1,3], n = 3))
print(sol.buildArray(target = [1,2,3], n = 3))
print(sol.buildArray(target = [1,2], n = 4))