# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        hashmap = {}
        for dominoe in dominoes:
            dominoe.sort()
            hashmap[tuple(dominoe)] = hashmap.get(tuple(dominoe), 0) + 1

        cnt = 0
        for key in hashmap:
            n = int(hashmap[key])
            cnt += ((n * (n - 1)) // 2)

        return cnt

sol = Solution()
print(sol.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]]))
print(sol.numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))