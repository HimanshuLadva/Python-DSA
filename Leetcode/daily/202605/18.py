# https://leetcode.com/problems/jump-game-iv/description/?envType=daily-question&envId=2026-05-18

from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        first = arr[0]
        last = arr[-1]

        set_arr = set(arr)

        if len(set_arr) == len(arr):
            return len(arr) - 1

        if len(arr) == 1:
            return 0
        if first == last:
            return 1
        else:
            return 3
    
sol = Solution()
sol.minJumps(arr = [100,-23,-23,404,100,23,23,23,3,404])