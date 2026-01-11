# https://leetcode.com/problems/happy-number?envType=problem-list-v2&envId=hash-table

class Solution:
    def isHappy(self, n: int) -> bool:
        arr = list(map(int, str(n)))
        ans = sum(x ** 2 for x in arr)
        if ans == 1:
            return True
        if ans == 4:
            return False
        print(ans)
        return self.isHappy(ans)
    
sol = Solution()
print(sol.isHappy(123))