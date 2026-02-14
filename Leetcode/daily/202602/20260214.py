# https://leetcode.com/problems/champagne-tower/description/?envType=daily-question&envId=2026-02-14
#howtowork
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (query_row+1) for i in range(query_row + 2)]
        tower[0][0] = poured

        for row in range(query_row):
            for glass in range(row + 1):
                if tower[row][glass] > 1.0:
                    overflow = tower[row][glass] - 1.0
                    tower[row + 1][glass] += overflow / 2
                    tower[row + 1][glass + 1] += overflow / 2
                    tower[row][glass] = 1.0
 
        return min(1.0, tower[query_row][query_glass])
    
sol = Solution()
poured = 15
query_row = 5
query_glass = 2
print(sol.champagneTower(poured, query_row, query_glass))