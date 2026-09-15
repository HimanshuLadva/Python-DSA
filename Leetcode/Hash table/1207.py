# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        freq2 = {}
        for f in freq:
            freq2[freq[f]] = freq2.get(freq[f], 0) + 1

            # print(freq[f])
            if freq2[freq[f]] > 1:
                return False

        return True

sol = Solution()
print(sol.uniqueOccurrences(arr = [1,2,2,1,1,3]))