# https://leetcode.com/problems/binary-watch/description/?envType=daily-question&envId=2026-02-17
from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(12):
            for j in range(60):
                x = bin(i).count('1')
                y = bin(j).count('1')
                if x + y == turnedOn:
                    ans.append(f"{i:01}" +':'+f"{j:02}")

        # print(f"ans length = {len(ans)}")
        return ans
    
sol = Solution()
print(sol.readBinaryWatch(1))
print(sol.readBinaryWatch(5))
        