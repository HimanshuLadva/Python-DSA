# https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        def solve(ans:list[int], idx: int) -> list[int]:
            if idx == rowIndex + 1:
                return ans

            ans.append(ans[idx-1] * (rowIndex - idx + 1) // idx)
            return solve(ans, idx + 1)

        return solve([1],1)

    #implogic
    #howtowork
    #revision
    def getRowV1(self, rowIndex: int) -> list[int]:
        row = [1]

        for i in range(1, rowIndex+1):
            next_ele = row[i-1] * (rowIndex - i + 1) // i
            print(f"next_ele = {next_ele}, row = {row[i-1], (rowIndex - i + 1)}, i = {i}")
            row.append(next_ele)

        print(row)
        return row

print(Solution().getRow(4))