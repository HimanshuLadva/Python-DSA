# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=problem-list-v2&envId=binary-search

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        difference = [target - numbers[0]]

        for i in range(1, len(numbers)):
            # print(i, numbers[i], difference, numbers[i])
            if numbers[i] in difference:
                idx = difference.index(numbers[i])
                return [idx+1, i+1]
            difference.append(target - numbers[i])

        return []

            

# print(Solution().twoSum(numbers = [2,7,11,15], target = 9))
print(Solution().twoSum(numbers = [2,3,4], target = 6))
# print(Solution().twoSum(numbers = [2,7,11,15], target = 18))