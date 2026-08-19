# https://leetcode.com/problems/arranging-coins/description/?envType=problem-list-v2&envId=math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        rows = n

        if n == 1:
            return 1

        for i in range(1, rows * 2):
            row += 1

            if n < i:
                return row-1

            n -= i
            
            if n == 0:
                return row
    
        return 0