from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s_arr = sorted(set(arr)) 
        rank = {num: i + 1 for i, num in enumerate(s_arr)}

        return [rank[num] for num in arr]
    
sol = Solution()
# print(sol.arrayRankTransform(arr = [40,10,20,30]))
print(sol.arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12]))