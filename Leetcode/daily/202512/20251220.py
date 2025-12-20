# https://leetcode.com/problems/delete-columns-to-make-sorted?envType=daily-question&envId=2025-12-20

from typing import List
class Solution:
    # 30ms
    # #note = *strs - this unpacks the list into separate arguments
    def minDeletionSize(self, strs: List[str]) -> int:    
        count = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                count += 1
        return count
    # 62ms
    def minDeletionSizeV1(self, strs: List[str]) -> int:    
        sn = len(strs[0])
        n = len(strs)
        count = 0
        for i in range(sn):
            temp = strs[0][i]
            for j in range(1,n):
                if temp > strs[j][i]:
                    count += 1
                    break
                temp = strs[j][i]
                # print(strs[j][i])
            # print(f'{count}======')
        return count
    
sol = Solution()
strs = ["cba","daf","ghi"]
strs = ["zyx","wvu","tsr"]
strs = ["rrjk","furt","guzm"]
print(sol.minDeletionSize(strs))