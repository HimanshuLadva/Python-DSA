# https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2026-05-06
from typing import List
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        
        for i in range(m):
            # print(boxGrid[i])
            # print(''.join(boxGrid[i]).split('*'))

            temp_arr = ''.join(boxGrid[i]).split('*')
            temp_len = len(temp_arr)
            
            for j in range(temp_len):
                new_str_len = len(temp_arr[j])
                hash_count = temp_arr[j].count('#')
                temp_arr[j] = '.'*(new_str_len - hash_count) + '#'*hash_count                

            boxGrid[i] = list('*'.join(temp_arr))
            # print(boxGrid[i])
        
        boxGrid[:] = list(zip(*boxGrid))
        boxGrid[:] = [list(row[::-1]) for row in boxGrid]
        return boxGrid
    
sol = Solution()
sol.rotateTheBox(boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]])