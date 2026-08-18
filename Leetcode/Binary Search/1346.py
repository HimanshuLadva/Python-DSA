# https://leetcode.com/problems/check-if-n-and-its-double-exist/?envType=problem-list-v2&envId=binary-search

from typing import List
from collections import defaultdict
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        lookup = defaultdict(int)

        for i in range(n):
            if arr[i] * 2 in lookup or (arr[i] % 2 == 0 and arr[i] // 2 in lookup):
                return True

            lookup[arr[i]] += 1
        return False

sol = Solution()
print(sol.checkIfExist(arr = [-10,12,-20,-8,15]))
print(sol.checkIfExist(arr = [10,2,5,3]))