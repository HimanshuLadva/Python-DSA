# https://leetcode.com/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23
from typing import List
from collections import defaultdict
#howtowork
#revision
#implogic
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        count = defaultdict(int)
        total = defaultdict(int)

        # Pass 1: left -> right
        for i in range(n):
            x = nums[i]
            res[i] += count[x] * i - total[x]

            count[x] += 1
            total[x] += i

        count.clear()
        total.clear()

        # Pass 2: right -> left
        for i in range(n - 1, -1, -1):
            x = nums[i]
            res[i] += total[x] - count[x] * i

            count[x] += 1
            total[x] += i

        return res
    
    #TLE
    def distanceV1(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = []
        for i in range(n):
            temp = 0
            for j in range(n):
                if j != i and nums[i] == nums[j]:
                    temp += abs(i - j)
            
            res.append(temp)
        return res

sol = Solution()
print(sol.distance(nums = [1,3,1,1,2]))